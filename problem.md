1. longi_lat_planner.hpp
* double longi_upper_limit_ = speed_limit_ * s_horizon_;是不是应该是*t_horizon_？
* ApplyFallBack功能？


2. parser.cpp
* else if (scenario_ == PlanningScenario::LANE_CHANGE): 现在不需要处理变道场景嘛？在object_map里面的constructSIntervals处理的变道吗？

3. predict_map.cpp
* cells_3d_.SetCell(
                    TripleToOne(t_index, sd_index.first, sd_index.second),
                    p_obj.id);这里用障碍物的id是能保证id<64的吗？或者可以用k来替换？

4. object_map.cpp
* if ((l_st.at(i).at(j) != 0) && (r_st.at(i).at(j) != 0)) 这里是不是应该排除掉上面判断不是nbo的obstacle id,例如前面两车，一车cut in,另一车骑线但是符合nbo
* // 4. calculate scenario when two nbos take both side of road and they are 这里好像没有进行筛选？
* nbo counter和bo counter是什么意义？为了保证使退出NBO更加严格吗？