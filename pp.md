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

# SQP思路整理(2020.05.06)
* planner_factory.hpp,PlannerFactory
  * CreatePlanner(): 根据配置文件返回生成的Planner(目前是LongiLatPlanner),并且对Planner进行Init
* base_planner.hpp,BasePlanner
  * Init(): 纯虚函数，仅调用一次
  * Update(): 每次由外界调用更新(roadStructure, predictionObject, dmTarget, vehicle_state)
  * Plan(): 纯虚函数，由子类完成规划
  * SetHondaConverter(): 输出结果
  * GetPlanningLog(): 传出PlanningLog(用于plotjuggler)
* longi_lat_planner.hpp,LongiLatPlanner
  * Init():初始化scene_interface_,searcher_,optimizer_(QP Optimizer or SQP Optimizer)
  * Plan():每帧进行调用，更新scene_interface, 调用Search，调用Optimize得到path
  * Search():调用searcher_.search()得到tag，以及搜索的结果
  * Optimize():更新optimizer.update, 进行优化optimizer.optimize
* parser.hpp,Parser
  * Init() 配置参数及初始化object_map
  * Update() 由Planner每帧进行调用，更新routing、障碍物、坐标系等状态，对object_map_对应的状态进行更新
    * object_map.Update() 更新状态
    * object_map.Refresh() 实际调用predict_map的Refresh()
    * object_map.FindNBO() 更新NBO状态
    * object_map.ConstructSIntervals() 忽略NBO构建ST图
    * object_map_.CutInLimitSpeed(&speed_ref_) 是否是cut in限速
  * GetObstacleCost() 在ST图中得到某个点的障碍物cost，由DP Searcher调用
  * SetObstacleTag() 根据在ST图规划的结果，将每个障碍物来做出超越或者跟车的决定
* sqp_optimizer.hpp,SQPOptimizer
  * Init() 初始化参数，初始化横纵向优化器，初始化fallback
  * Optimize() 进行优化得到路径
    * UpdateCachedPath() 更新上一帧轨迹，进行备用
    * LongitudinalOptimize() 横向规划得到结果
  * LongitudinalOptimize()
    * scene_interface_.GetLongiBoundAndRef()：得到s上下边界(根据dp的tag)以及参考线，在sqp中只用到了supper和slower
    * ResetlongiBound()：根据初始速度和动力学来更新vupper，aupper，alower
    * SetSpeedScene()：判断场景
    * RunSpeedMpcPlanner()：调用优化器求解
* optimal_speed_planner.hpp,OptimalSpeedPlanner
  * InitalOptimalPLanner() 初始化优化器及参数
  * RunSpeedMpcPlanner()：对现在的定义进行求解

# 任务完成
## 障碍物筛选 https://confluence.sensetime.com/pages/viewpage.action?pageId=142311902
## Cutin https://confluence.sensetime.com/pages/viewpage.action?pageId=150332478
## NBO绕行速度设计 https://confluence.sensetime.com/pages/viewpage.action?pageId=142318242
## PP工具设计 https://confluence.sensetime.com/pages/viewpage.action?pageId=150339139

