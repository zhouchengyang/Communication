#### 2020.1.4

运动规划的分享

1. 运动规划Intro & Mpc
2. 纵向规划设计
3. 横向规划设计
4. 求解失败后处理

#### 2020.1.5

1. 解决s v t问题，更加连续以及不贵出现规划轨迹忽长忽短
2. 会出现速度变化比较大导致曲率比较小的问题
3. 偶发性的限速(qp在一定的加速度下突然限速无解，不应该有这个突然限速)
4. 优化时考虑曲率

#### 2020.1.6

1. dm新加的change flag
2. 过一下仿真集合

#### 2020.1.7

1. 完成pp分享（总结一下）
   1. 会前认真准备，不要被其他因素影响
   2. 平时多思考，多积累
   3. 锻炼把事情讲清楚的能力

#### 2020.1.8

1. 对急刹车case
2. 制定下个季度的OKR
3. 周总结



#### 2020.1.11

1. 分析数据，整理周报
2. 调研阿波罗参考线优化

### 2020.1.12

1. 增加参考线曲率
2. 仿真UTURN和Turn Left

#### 2020.1.13

1. 仿真得出结论
2. 与发哥讨论

#### 2020.1.14-2020.1.15

1. 基本搞定参考线平滑，还剩两个问题
2. 连续变道代码基本实现，发现dm发的连续变道flag与第一次变道flag不匹配



#### 2020.01.18

1. 开会
2. 搞一下连续变道的问题
   1. 对虚拟障碍物做两部分处理
3. 重新弄一个单例模式

#### 2020.01.20

1. 测试单例模式
2. 开会(超车的阈值以及sdk重构的内容)
3. 合入单例模式和横向无解bug 8010，8049
4. 看横向规划代码
   1. 横向dp计算前一点与当前点的cost时第二点d的设计

#### 2020.01.21

1. 画图画的不准确
2. 有一些奇怪的点
3. 修复横向dp两个问题，调整了下横向dp的光滑性 8069
4. 连续变道

#### 2020.01.22

1. 连续变道测试
2. 修复横向错误的s seq
3. 静止起步慢，keep onsite减速巡航，减速之后加速慢



#### 2020.01.25

1. 开会

#### 2020.01.26

1. dp平滑性搞定，进行测试

#### 2020.01.27

1. 平滑性合入
2. 参考线优化
3. 解了一个曲率正负的问题
4. 几何学上运动过去解了

#### 2020.01.28

1. 仿真参考线优化
2. 思考纵向S-V限速
3. VNC远程



#### 2021.02.01

1. 适配了实线边界
2. 修复bug
   1. 增加界面
   2. 现有地图
3. 连续变道已解决
4. 参考线优化的横向边界

#### 2021.02.02

1. 修复参考线优化的横向边界
   1. 参考线优化时离横向边界过近(调整权重)
   2. 参考线优化之后，横向优化实现边界不对(尝试方法)

####  2021.02.03

1. 修复参考线优化的虚拟障碍物

#### 2021.02.04

1. 修复参考线优化出现的一个bug
   1. 变道超调之后pp变道方向与dm不同
   2. 过ci，进行测试

#### 2021.02.05

1. 提7528路测
2. 对急刹和接管case
3. 构建sv



#### 2021.02.18

1. 想看7528数据，数据平台有问题
2. 编写sv，学习C++

#### 2021.02.19-20

1. 修复隐含变道之后参考线变化问题
2. 总结优化后参考线特点
3. 验证高速时减小曲率功能
4. 减少最大曲率
5. 完成Speed Bound Decider
6. 找横向无解的bug



#### 2021.02.22

1. 改成后轮中心
2. 发现边界问题

#### 2021.02.23

1. 测试7528
2. 速度边界

#### 2021.02.24

1. 修复7528参考线离实线过近的问题
   1. 发现在参考线优化时横向边界挑了很多
   2. 发现横向虚拟障碍物跳变



#### 2021.03.01

1. 测试7528
2. 发现横向有时无解的bug
3. 修复7528问题

#### 2021.03.02

1. 修改7528虚拟障碍物实线点的选择
2. 生成arm版本的.so
3. 可视化轨迹
   1. 在frenet向前平移不行
   2. 按照一定的方向平移不对
   3. 去掉前一段轨迹
4. 合入7528

#### 2021.03.03

1. 合入7528
2. 仿真7887
3. 完成SQP以及限速的测试
4. 完成纵向dp的一部分

#### 2021.03.05

1. 发现虚拟障碍物横向tag不对的问题(发哥接)
2. 发现参考线replan flag不对的问题
3. 连续变道不对的问题
4. CIplanning有挂的问题(未接)



#### 2021.03.06

1. 开会，分case
2. 解决变道限速的问题，合入代码
3. 进入自动驾驶状态，自车参考线不更新，回放不启动DM节点时，自车参考线不更新

#### 2021.03.07

1. 合入8428
2. 合入8520
3. 测试精细的速度规划边界



#### 2021.03.12

1. 完成自己生成参考线变化的flag
2. 增加在非junction内部更加贴近参考线的权重
3. 测试了精细化的速度边界
4. 参考线优化掉头成直线



#### 2021.03.15

1. 合入8557
2. 周报

#### 2021.03.16

1. 发现测试问题
2. 继续测试7887
3. 修复横向ref变化导致自车s型
   1. 前n维度如果不碰撞尽量与上一帧接近
   2. 不能全部，因为可能会导致绕行不足

#### 2021.03.17

1. 看7887的测试数据，增加变道加速功能
2. 测试横向优化ref的参考
3. 合入master

#### 2021.03.18

1. 合入7887
2. 测试8195
3. 行人横穿

#### 2021.03.19

1. 分数据
2. TODO 预防减速
3. TODO Merge
4. TODO 行人横穿

#### 2021.03.22

1. 周报
2. 适配DP
3. 仿真case8195

#### 2021.03.23

1. 修复在路口绕行过多
2. 修复绕行vru减速过早的问题

#### 2021.03.24

1. 提出proposal
2. 修复变道时调用纵向优化的bug

#### 2021.03.25

1. 配置环境
2. 找8687的bug

#### 2021.03.26

1. 增加

