# QPP函数思路整理(2020.03.31)
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
    * LongitudinalSearch() 利用DP搜索st轨迹得到初步结果
    * ApplyFallBack() 搜索失败，急刹车
    * LongitudinalOptimize() 纵向Qp优化
    * LateralOptimize() 横向Qp优化
    * FillupTrajectory() 根据横纵向结果来得到轨迹sdt
* Parser
  * Init() 配置参数及初始化object_map
  * Update() 由Planner每帧进行调用，更新routing、障碍物、坐标系等状态，对object_map_对应的状态进行更新
    * object_map.Update() 更新状态
    * object_map.Refresh() 实际调用predict_map的Refresh()
    * 
* PredictMap
  * Init() 配置参数及初始化cell_3d
  * Update() 由ObjectMap进行调用，更新内部routing、障碍物、坐标系等状态，同时对obs_screen, cell_3d进行更新
  * Refresh() 由Parser进行每帧更新， 清空cell_3d，根据障碍物的预测轨迹来填充cell_3d，cell_3d表示障碍物在sdt的占据(同时包含了对不影响当前轨迹障碍物的筛选)
* ObjectMap:public PredictMap
  * Init() 配置参数及初始化predict_map
  * Update() 由Parser调用，用于更新内部routing、障碍物、坐标系等状态，同时对predict_map进行更新
* ObstacleScreen
  * Update() 更新坐标系、障碍物、routing、当前位置等信息
  * IsIgnore() 传入障碍物，根据若干条件进行障碍物筛选，从而得到本障碍物忽略类型(不忽略，本帧忽略，之后帧均忽略)
