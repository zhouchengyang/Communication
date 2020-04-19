# DQQ函数思路整理(2020.03.31)
* BasePlanner
  * CreatePlanner() -> bpp_ptr外界调用传入配置文件并返回planner指针
  * Init() 纯虚函数，由子类继承调用
  * Plan() 纯虚函数，由子类继承调用，规划的主函数，由外界调用并返回规划结果
  * Update() 更新frenet坐标系，更新障碍物，routing以及dm目标(scene_parser_)
  * BuildFrenetCoordSystem() 更新frenet坐标系，由Update调用更新
* LongiLatPlanner:public BasePlanner
  * Init() 继承而来，由CreatePlanner进行调用，初始化配置、frenet_system、scene_interface(Parser类)、searcher、optimizer等初始化，仅执行一次
  * Plan() 继承而来，由上层调用，执行多次,执行以下功能
    * UpdateInitalState() 更新当前初始状态(理想更新或者实际更新)，
    * PlanningState2VehicleState() 将出发点frenet坐标系下转化为真实坐标
    * sence_interface_.Update() 更新scene_interface_里面的障碍物、坐标系、换道方向和当前位置
    * UpdateCachedPath() 更新上一帧轨迹，以便用于备份
    * LongitudinalSearch() 利用DP搜索st轨迹得到初步结果，如果搜索失败，将所有的障碍物设置为yeild
    * ApplyFallBack() 搜索失败，进行碰撞检查来决定是使用上一帧轨迹或者急刹车
    * LongitudinalOptimize() 纵向Qp优化,根据DP搜索得到的轨迹以及障碍物来得到优化边界,根据参考速度和参考线来优化，最终末速度根据NBO最大速度来选
    * LateralOptimize() 横向Qp优化，根据纵向得到的结果来获取横向规划边界，参考线按照变道和不变道来取
    * FillupTrajectory() 根据横纵向结果来得到轨迹sdt
* Parser
  * Init() 配置参数及初始化object_map
  * Update() 由Planner每帧进行调用，更新routing、障碍物、坐标系等状态，对object_map_对应的状态进行更新
    * object_map.Update() 更新状态
    * object_map.Refresh() 实际调用predict_map的Refresh()
    * object_map.FindNBO() 更新NBO状态
    * object_map.ConstructSIntervals() 忽略NBO构建ST图
  * GetObstacleCost() 在ST图中得到某个点的障碍物cost，由DP Searcher调用
  * SetObstacleTag() 根据在ST图规划的结果，将每个障碍物来做出超越或者跟车的决定
* PredictMap
  * Init() 配置参数及初始化cell_3d
  * Update() 由ObjectMap进行调用，更新内部routing、障碍物、坐标系等状态，同时对obs_screen, cell_3d进行更新
  * Refresh() 由Parser进行每帧更新， 清空cell_3d，根据障碍物的预测轨迹来填充cell_3d，cell_3d表示障碍物在sdt的占据(同时包含了对不影响当前轨迹障碍物的筛选)
* ObjectMap:public PredictMap
  * Init() 配置参数及初始化predict_map
  * Update() 由Parser调用，用于更新内部routing、障碍物、坐标系等状态，同时对predict_map进行更新
  * FindNBO() 更新NBO相关状态
    * GetLateralRange() 根据当前是否变道获取左右车道边界
    * nbo_handler.Update() 更新车道边界、坐标系、目标车道以及障碍物，并且判断每个障碍物是否为NBO
      * Handle() 根据车辆可行边界判断NBO，排除VRU(车辆行人)，同时考虑上一帧的NBO来提高连续性，对于消失的NBO进行处理
      * CalcNBOSpeedAndDistance() 计算NBO的最远距离和最大速度
    * nbo_handler.GetNBO() 判断障碍物是否为NBO，返回NBO的id
    * nbo_handler.GetNBODistance() 得到NBO的最远距离
    * nbo_handler.GetNBOSpeed() 得到NBO的最大速度
  * ConstructSIntervals() 忽略NBO构建ST图
* ObstacleScreen
  * Update() 更新坐标系、障碍物、routing、当前位置等信息
  * IsIgnore() 传入障碍物，根据若干条件进行障碍物筛选，从而得到本障碍物忽略类型(不忽略，本帧忽略，之后帧均忽略)
# Optimal motion planner思路整理(2020.04.01)
* OptiMotionPlanner:public BasePlanner
  * Init() 与LongiLatPlanner::Init()基本相同，不同点在于初始化optimal_lat_planner和optimal_longi_planner两个不同的横纵向优化器
  * Plan() 与LongiLatPlanner::Plan()基本相同
    * LongitudinalOptimize() 
    * LateralOptimize() 

## Cutin
### 背景
cut in主要是为了解决在他车缓慢cut in时预测轨迹不及时进入当前车道所产生的问题，因此最主要的目标是提前识别出他车缓慢cut in的意图并且能够做出避让处理。判断他车cut in意图的条件要较为严格，不然会导致一些误刹车，因此要在各个维度来限制判断的条件：
### 识别条件
1. 纵向位置(下面条件均符合)
* 他车车头在自车质心前方，在自车质心后方的车辆正常情况下无法cut in
* 他车车尾不超过自车车头一定位置(10m)，超过一定位置切入进来的情况由规划来解决
2. 横向位置(下面条件均符合)
* 两车横向距离应小于一定值，只有在较为横向较为靠近的车会有缓慢cut in的问题，删除不需要分析的车辆
* 两车横向不应该重叠，在重叠时交由规划处理
3. 横向速度(符合下面的条件之一)
* 当他车横向接近速度较大时，说明他车有cut in的意图
* ttc小于一定值，说明较为可能发生危险(ttc = d / (v_ego - v_obs))
### 退出条件
为了防止障碍物cut in状态频繁跳转，设定连续n帧丢失cut in状态的障碍物退出cut in模式
### 识别后的解决思路
在识别到他车有cut in意图时，自车可以采取横向和纵向两个方向来避让。
1. 横向避让
横向避让在自车或者他车速度较高时风险系数比较大，且在实现上复杂，暂不考虑。
2. 纵向避让
纵向避让主要是设置自车速度的上限值来保证对他车的避让。相对于他车轨迹突然进入当前车道导致的急刹车，这种方案能够提前识别他车意图，从而有更长的反应时间，同时能够减少规划的压力，使速度规划更加平稳、舒适。
### 代码实现

### 仿真案例