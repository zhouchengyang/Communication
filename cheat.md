# Cheat && Summary
## 配置环境
1. 新手教程任务1：https://confluence.sensetime.com/pages/viewpage.action?pageId=101900275
2. 二进制发布中的key
    aws configure --profile ad_system_common
    AWS Access Key ID [None]:O5B34FE51MMZRZGEY1Z5
    AWS Secret Access Key [None]:Xh6hOX5xnZ6BrsNnCcCt8NzNCbWeCSYwtABErKJ6
    Default region name [None]:
    Default output format [None]:
3. 创建docker容器
CanlibSO=$(find /usr/lib/ -name 'libcanlib.so*' -exec echo "-v {}:{} " \;)
DriverMajorVersion=$(nvidia-smi --query-gpu=driver_version --format=csv,noheader | head -n 1 | cut -d '.' -f 1)
docker run -it  --privileged --runtime=nvidia --name senseauto \
    -e NVIDIA_VISIBLE_DEVICES=all \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /usr/lib/nvidia-${DriverMajorVersion}:/usr/lib/nvidia-${DriverMajorVersion} \
    -v ${HOME}/docker_ws:/home/sensetime/ws \
    -v ${SENSEAUTO_LOCAL_DIR}:${SENSEAUTO_LOCAL_DIR} \
    ${CanlibSO} \
    -v /usr/include/canlib.h:/usr/include/canlib.h \
    -v /usr/doc/canlib:/usr/doc/canlib \
    -v /usr/include/canstat.h:/usr/include/canstat.h \
    -v /usr/include/obsolete.h:/usr/include/obsolete.h \
    senseauto-dev:my-image /bin/bash
## 常用命令
1. docker相关：
* 启动docker
docker start senseauto
docker attach senseauto
* 退出docker
ctrl+d
2. 同步相关：
* 和远程同步
cd ~/docker_ws/repo_pro/senseauto
./system/scripts/repo/sync.sh
* git操作
git status
git log --graph --oneline --branches --all --decorate
git lg
git add file, git reset file
git diff --staged
git commit -m "commit message"
git commit --amend
git pull origin master
git push origin master
git help
* commit规范
AUTODRIVE-2428 repair speed too high bug
 
* Speed is too high, which is dangers.
* Took Throttle as Brake.
* Correctly handle throttle and brake.

* 多个commit合并
https://github.com/Jisuanke/tech-exp/issues/13
3. 编译仿真：
* 在docker内部更新
cd /home/sensetime/ws/repo_pro/senseauto
./system/scripts/binary_release/configure.sh
./system/scripts/binary_release/check_version_and_update_package.sh
* 在docker内部编译
cd ~/ws/repo_pro/senseauto/build && cmake ..
make -j4
* 开启仿真
cd ~/ws/repo_pro/senseauto/ && ./system/launcher/simulator.sh -r -m 3
* 启动plotjuggler
rosrun plotjuggler PlotJuggler
5. tmux：
* 启动与退出
tmux
ctrl+d 或者 exit 表示直接退出
* 会话管理
tmux ls 列出所有tmux会话
tmux detach 将当前会话隐藏到后台
tmux attach -t number 调出来会话number
tmux kill-session -t number 杀掉会话
tmux switch -t number 转到另一个会话
tmux kill-server 关闭所有会话
* 窗格管理(以下命令均需要加前缀ctrl+b，且需要在tmux下输入)
% 划分为左右窗口
" 划分为上下窗口
箭头 切换到某个方向的窗格
; 切换到上一个窗格
o 切换到下一个窗格
z 当前窗格全屏显示
q 显示所有窗格编号
