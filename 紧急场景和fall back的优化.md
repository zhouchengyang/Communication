紧急场景的定义和fall back的优化

非紧急场景

<img src="/Users/zhouchengyang/Library/Application Support/typora-user-images/image-20200731144656404.png" alt="image-20200731144656404" style="zoom: 67%;" />



紧急场景需要减速

<img src="/Users/zhouchengyang/Library/Application Support/typora-user-images/image-20200731145314703.png" alt="image-20200731145314703" style="zoom:60%;" />2020_07_30_21_26

<img src="/Users/zhouchengyang/Library/Application Support/typora-user-images/image-20200731152038686.png" alt="image-20200731152038686" style="zoom:67%;" />2020_07_30_21_26

<img src="/Users/zhouchengyang/Library/Application Support/typora-user-images/image-20200731152521449.png" alt="image-20200731152521449" style="zoom:67%;" />2020_07_30_21_16

<img src="/Users/zhouchengyang/Library/Application Support/typora-user-images/image-20200731184334008.png" alt="image-20200731184334008" style="zoom:67%;" />

紧急场景需要急刹车

<img src="/Users/zhouchengyang/Library/Application Support/typora-user-images/image-20200731150159420.png" alt="image-20200731150159420" style="zoom:67%;" />2020_07_30_21_23_13

<img src="/Users/zhouchengyang/Library/Application Support/typora-user-images/image-20200731183818235.png" alt="image-20200731183818235" style="zoom:67%;" />2020_07_30_21_36_54



需要再想想

## fallback存在的几个问题

1. 比较近的红绿灯或者比较近的障碍物(10-30m左右)，会无解并且利用上一帧的无减速轨迹，浪费一些制动距离
2. 在输入leader s比较近或者比较切入距离比较近的时候，容易进入匀jerk模型

## 修改思路

fallback定义是求解失败后进行重新求解的过程，有几种思路来做

1. 考虑刹停在前车进入安全车道的位置
2. 不考虑上一帧轨迹，仅考虑避让安全车道车尾的leader(优势是与优化问题比较一致的输入，不需要设置比较奇怪的东西)()

## 最终思路   

1. 求碰撞点（自车质心所在位置与前车过近）
2. 更新上一帧碰撞点(无解第一帧计算碰撞点，后续持续更新更近碰撞点)
3. 将碰撞点设置为leader

期望解决问题：

1. 不设置比较奇怪的条件，尽量用优化来求
2. 不会出现一帧有解一帧无解导致溜车的问题

## 测试结果

<img src="/Users/zhouchengyang/Library/Application Support/typora-user-images/image-20200816141116042.png" alt="image-20200816141116042" style="zoom:67%;" />

<img src="/Users/zhouchengyang/Library/Application Support/typora-user-images/image-20200816142007376.png" alt="image-20200816142007376" style="zoom:67%;" />

测试结论：

1. 在无解的情况下较少进入匀jerk，整体体验较好(发现两个bug)
2. 前车急刹车时(前车速度误差大)
3. 纵向安全性不够(1. 收到前车时间晚，减速力度小)