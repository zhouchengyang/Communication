# 2020.03.10-2020.03.13
1. 注册了各个网站(OA, Ehr, It, Mail, ubuntu)并修改密码，半天
2. 浏览自动驾驶DPC的Confluence，半天
3. 查看PP的相关界面，半天
4. 按照新员工操作练习任务一配置环境，一天半(https://confluence.sensetime.com/pages/viewpage.action?pageId=101900275)
   1. 权限添加：获得了gerrit.sensetime.com权限，加入了ADR&D邮件组，获得了senseauto_binary_release的公共aws key
   2. 配置二进制开发系统环境
   3. 配置git lfs账号
   4. 下载senseauto代码以及配置gerrit和repo
   5. 部署docker环境，在docker环境下完成程序的编译链接
   6. 问题：
      1. 权限未获取:找leader和zhangshu分别获取权限，并完成aws的配置(不然无法下载二进制编译数据)
      2. repo拉取文件错误:可能是因为git lfs版本未更新至最新
      3. cmake failure:主机代码未更新至最新
5. 参与登科和升发关于NBO障碍物筛选的讨论 半天
6. 了解并运行rviz模拟器，配置vpn(身体原因远程办公) 半天
## 2020.03.16
1. 学习git操作，并且完成练习， 半天
2. 每周例会， 半天
3. 学习如何使用rosrun plotjuggler和tmux来仿真
## 2020.03.17
1. 学习Vim和tmux
2. 阅读代码：
   1. 变量
   2. 文件
## 2020.03.18
1. 学习git的操作
2. 阅读并运行代码
   1. baseplanner, planner, dp_searcher,st_graph_searcher, longi_lat_planner
## 2020.03.19
1. 阅读代码
   1. predict_map, object_screen, longi_lat_planner剩余的函数
## 2020.03.20
1. 阅读代码
   1. parser， obstacle_map
2. 学习Linux技巧
## 2020.03.23
1. 阅读代码
* Init: Base_planner::Create_planner, Longi_lat_planner::Init, Parser::Init, Object_map::Init, Predict_map::Init
* Update: Base_planner::Update, Base_planner::BuildFrenetCoordSystem
* Update: Longi_lat_planner::Plan, Parser::Update, Object_map::Update, Predict_map::Update
* Update: Predict_map::Refresh, Object_map::FindNBO, Object_map::ConstructSIntervals
* Update: Longi_lat_planner::UpdateCachedPath
2. 开会(下午周例会， 晚上会议)
## 2020.03.24
1. 阅读代码
* Update：Longi_lat_palnner::UpdateInitState, DPSearcher::Update, DPSearcher::Search
* Update: Longi_lat_planner::LongitudinalOptimize, Longi_lat_planner::LateralOptimize
* Update: Longi_lat_planner::EmergencyBrake, Longi_lat_planner::ApplyFallBack
2. 查看config参数及confluence
## 2020.03.25
1. 仿真(HMI和Ros PlotJuggler)
2. 仿真bag和场景编辑，OKR小组讨论
## 2020.03.26
1. 仿真HMI以及场景编辑器
2. aws路测数据下载
3. 仿真调试流程熟悉
## 2020.03.27
1. 仿真场景打tag
2. 分析场景
3. 阅读代码

## 2020.03.30
1. 周会
2. 0327仿真场景打tag
3. 阅读代码
## 2020.03.31
1. 阅读谷歌代码规范
2. 整理pp代码思路
3. 分析0330数据

## 2020.04.01
1. 整理规划dqq
2. 分析0331数据
## 2020.04.02
1. Q2OKR会议
2. Q2OKR整理
3. 阅读OMP
## 2020.04.03
1. 阅读OMP
2. Q2OKR整理
3. cut in思路整理

## 2020.04.07
1. Q2OKR整理
2. 缓慢cut in confluence思路
## 2020.04.08
1. 障碍物筛选整理
2. 障碍物筛选case梳理
3. 分析0402数据
## 2020.04.09
1. 障碍物筛选代码
2. 回流case
3. 学习repo，新建分支
4. 缓慢cutin讨论
## 2020.04.10
1. 缓慢cut in代码编写
2. 回放case
3. 组会分享

## 2020.04.13
1. 障碍物筛选(对于大车来说label只有在回放的时候才有，在本地仿真的时候就没有)
2. 整理障碍物筛选相关case()
3. 提交代码到gerrit
4. 提交路测
## 2020.04.14
1. 整理cut in的case
2. 安装clang format 3.8
3. 编写cut in代码
4. daily test会议
## 2020.04.15
1. 修复变道障碍物筛选的issue
2. 编写cut in代码
3. 用每个case来测试obs分支
4. 发现障碍物筛选的bug并提交路测
## 2020.04.16
1. 修改不同obs代码
2. 测试每个障碍物筛选的case
3. 发现可视化HMI bug
## 2020.04.17
1. 分析路测数据
2. 完善缓慢cut in情况
3. 周报分析

## 2020.04.20
1. 周报，合入代码
2. 修改cut in逻辑
3. 学习C++
## 2020.04.21
1. 完成cut in代码
2. 进行多组仿真测试
## 2020.04.22
1. 完成cut in代码测试
2. PP工具设计思路整理
## 2020.04.23
1. 分析路测数据
2. 仿真数据分析
3. 读OMP代码

## 2020.04.27
1. 合入cut in代码
2. 组会4个小时