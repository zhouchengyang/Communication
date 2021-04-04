QP：Quadratic Programming

$$
\frac{1}{2} x^THx+f^T x\\
s.t. LB \leq x \leq UB\\
A_{eq}x=b_{eq}\\
Ax\leq b
$$
是指目标为二次函数，约束是线型等式或者不等式的优化问题叫做二次规划；需要H为半正定矩阵，才是一个凸问题；对于此类问题可以采用ASM(有效集方法)，有效集方法是指通过计算不同的有效约束来找最小cost的方法；同时也可以用[内点法](https://blog.csdn.net/dymodi/article/details/46441783),包括障碍物点法，Primal-Dual Method
$$
\frac{1}{2} x^THx+f^T x\\
s.t. A_{eq}x=b_{eq}\
$$
对于只有等式约束的问题可以采用拉格朗日乘子法，首先定义拉格朗日函数然后在求解方程。

对于既有不等式也有等式约束的需要KKT条件，首先定义L函数，之后设置符合最小值的kkt条件



