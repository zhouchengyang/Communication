# 2020Q2
## 2020.03.10-2020.03.13
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
## 2020.04.28
1. 合入代码
2. 修改nbo限速有关以及逻辑
## 2020.04.29
1. 搬家
## 2020.04.30
1. 修改nbo限速逻辑

## 2020.05.06
1. 修改nbo限速逻辑以及仿真
2. 周报以及任务整理

## 2020.05.07
1. PP代码整理
2. 看障碍物筛选以及一两个case
## 2020.05.08
## 2020.05.09
1. 分析case
2. 合如nbo限速
3. 增加hmi degug
4. 阅读sqp方法

## 2020.05.11
1. 周会
2. PP debug信息设计
## 2020.05.12
1. PP debug设计代码提交
2. dm2.5红绿灯逻辑修复
## 2020.05.13
1. PP debug设计代码修复
2. 红绿灯刹车逻辑
## 2020.05.14
1. 阅读SQP代码，改善速度规划
## 2020.05.15
1. Issue整理
2. 测试红绿灯刹车逻辑

## 2020.05.18
1. 周会整理
2. 修改SQP代码，尽量将刹车合入master
## 2020.05.19
1. 调试刹车参数
2. 修改SQP代码，并且调试
## 2020.05.20
1. 合入刹车代码
2. 整理sqp改进思路,不确定性的处理
## 2020.05.21
1. 整理路测case
2. cut in数据分析
3. 不确定性处理，完成代码
## 2020.05.22
1. 不确定性处理，进行测试
2. 解决QP存在的问题
3. 障碍物筛选的问题

## 2020.05.25
1. 修改qp不确定性代码，进行测试
2. 分析路口cut in以及新问题
## 2020.05.26
1. 分析路测问题，进行统计
2. qp不确定性代码及测试(4345, 4834, 4883, 4619)
3. qp速度参考的问题(4846)
3. cut in阈值分为缓慢cut in和紧急cut in(4958, 4880)
## 2020.05.27
1. 分析路测问题
2. 测试cut in参数(已提交)
3. 解决他车近距离导致的无解问题(思考)
## 2020.05.28
1. 阅读代码(障碍物筛选，纵向优化边界，横向优化边界，求解失败，障碍物投影，变道过程)
## 2020.05.29
1. 阅读代码并且分析Q2 daily test

## 2020.06.01
1. 阅读代码，分析路测case
## 2020.06.02
1. 阅读代码，分析路测

## 2020.06.08
1. 分析路测case
2. 开会以及制定本周计划
3. 分析路测case 更新dqq v1.0
## 2020.06.09
1. 分析路测case 更新dqq v1.0
2. 阅读代码，看qp仿真结果
## 2020.06.10
1. 更新dqq v1.0
2. 分析紧急cut in的case
3. 完成代码阅读以及障碍物筛选
## 2020.06.11
1. 阅读代码以及障碍物筛选(完成)
## 2020.06.12
1. 合入qp不确定性
2. 分析问题，阅读代码
3. 统计dqq v1.0

# 2020Q3

## 2020.06.30

1. HdMap2.0 PP代码适配

## 2020.07.01

1. HdMap2.0 代码适配
2. 前车急刹自车安全性分析
3. 路测数据分析
4. Hdmap2.0开户

## 2020.07.02

1. 急刹数据分析
2. OKR整理
3. 删除High V

## 2020.07.03

1. 安装黑苹果，并且学习苹果系统的使用



## 2020.07.06

1. 合入删除high v场景
2. 分析接管数据

## 2020.07.07

1. 解决加速过猛的问题
2. 设计s ref线型和cost

## 2020.07.08

1. 整理路测case，与dqq2.0
2. 解决high v的bug

## 2020.07.09

1. 整理急刹车case
2. 跟科哥修复了一个bug

## 2020.07.10

1. merge场景分析
2. merge方案设计

