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
cd ~/docker_ws/repo_pro/senseauto && ./system/scripts/repo/sync.sh

* git操作[https://confluence.sensetime.com/pages/viewpage.action?pageId=37291981]
git status
git log --graph --oneline --branches --all --decorate
git lg
git add file, git reset file
git diff --staged
git commit -m "commit message"
git commit --amend
git commit -a –amend --no-edit 直接提交没有新的commit
git pull origin master
git push origin master
git help
git branch <name>
git checkout branch-name
git checkout -b <name> # 上述两条命令之和
git checkout <name> && git merge <name2> 将name2合并到name1分支
git branch -b <name> 删除name分支
git fetch origin
git push origin <name>
git push origin HEAD:refs/for/master%topic=A

* commit规范
```
AUTODRIVE-2428 repair speed too high bug
 
* Speed is too high, which is dangers.
* Took Throttle as Brake.
* Correctly handle throttle and brake.
```
* 多个commit合并
  https://github.com/Jisuanke/tech-exp/issues/13

* 下载topic
  repo download-topic AUTODRIVE-`0000_Create_Branch_MyBranch`
  repo sync -d -j4 

* 下载二进制包

  ./system/scripts/binary_release/download.py interaction -i prebuild/ --topic AUTODRIVE-5632_fix_bug_of_fallback

3. 编译仿真：
* 在docker内部更新
  cd ~/ws/senseauto
  ./system/scripts/binary_release/configure.sh
  ./system/scripts/binary_release/check_version_and_update_package.sh

* 在docker内部编译
  cd ~/ws/senseauto/build && cmake .. && make -j4

* 开启仿真
  cd ~/ws/senseauto/ && ./system/launcher/simulator.sh -r -m 3
  打开localhost:8082
  运行自定义场景数据 ./system/launcher/simulator.sh  -s ~/data/Download/scenario.zip
  运行下载文件后的场景数据 ./system/launcher/simulator.sh  -s ~/data/data/path/simulator_scenario/0
  运行下载文件后的场景数据 ./system/launcher/simulator.sh  -s ~/data/data/path/simlator_scenario/simulator_scenario_log.bin -t 2020-03-xx-xx-xx-xx
  运行bag数据 ./system/launcher/simulator.sh -m 4 -k ~/data/Download/xxx.bag
  运行bag数据 ./system/launcher/offline_play_dmppcl.sh ~/data/data/case/

* 启动plotjuggler
  rosrun plotjuggler PlotJuggler

* config文件:
  /system/config/pp_config.ini

* 输出日志文件:
  vim /tmp/ros_decision_planning_node.txt 

* 画出dpqp过程
  python3 ~/ws/senseauto/modules/path_planning/scripts/plot_dqq_process.py -d /tmp/today-logs/ -t 2020-03-18-14-44-14

* 场景编辑器
  cd ~/ws/repo_pro/senseauto/modules/simulator/tools/scenario_editor/ && ./auto_start.sh
  打开locahost:8085

* 临时增加cut in or lead

* hub挂掉可以尝试
  repo forall -c "git lfs pull"
  打开新的tmux窗口
  cd ~/ws/senseauto/modules/simulator/scripts/manual_control
  ./control.py cutin
  ./control.py lead
  修改参数：cutin.yaml

* 第三方库编译流程

  本地编译：进入docker，找到mpc_lon_code_generator/code_generation.sh

  远程编译：ssh nvidia@10.151.176.84 找到zhouchengyang，然后进入code_generation.sh

4. tmux：
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

5. linux
* 文件
bin 存放二进制可执行文件(ls,cat,mkdir等)
boot 存放用于系统引导时使用的各种文件
dev 用于存放设备文件
etc 存放系统配置文件
home 存放所有用户文件的根目录
lib 存放跟文件系统中的程序运行所需要的共享库及内核模块
mnt 系统管理员安装临时文件系统的安装点
opt 额外安装的可选应用程序包所放置的位置
proc 虚拟文件系统，存放当前内存的映射
root 超级用户目录
sbin 存放二进制可执行文件，只有root才能访问
tmp 用于存放各种临时文件
usr 用于存放系统应用程序，比较重要的目录/usr/local 本地管理员软件安装目录
var 用于存放运行时需要改变数据的文件
* 可执行文件的分类
内置命令：出于效率的考虑，将一些常用命令的解释程序构造在Shell内部。
外置命令：存放在/bin、/sbin目录下的命令
实用程序：存放在/usr/bin、/usr/sbin、/usr/share、/usr/local/bin等目录下的实用程序
用户程序：用户程序经过编译生成可执行文件后，可作为Shell命令运行
Shell脚本：由Shell语言编写的批处理文件，可作为Shell命令运行
* 通配符
*：匹配任何字符和任何数目的字符
?：匹配单一数目的任何字符
[ ]：匹配[ ]之内的任意一个字符
[! ]：匹配除了[! ]之外的任意一个字符，!表示非的意思
* 常用命令
可用pwd命令查看用户的当前目录
可用cd命令来切换目录
.表示当前目录
.. 表示当前目录的上一级目录（父目录）
- 表示用 cd 命令切换目录前所在的目录
~ 表示用户主目录的绝对路径名
脱域：i have no name找it

* Kazam
https://ywnz.com/linuxrj/2762.html
* super+ctrl+q 退出
* super+ctrl+r 开始录制
* super+ctrl+f 退出录制
* super+ctrl+p 暂停
* ctrl+alt+a 截图需要配置

6. aws操作
* aws 配置：aws configure 输入邮件中的key和id
* aws 列出：aws s3 ls s3://Field_Test_Data/master/segment_data/2020_xx_xx/CN017/DPC/take_over/
* aws 列出：aws s3 ls s3://Field_Test_Data/master/raw_data/
* aws 下载目录：aws s3 cp s3://Field_Test_Data/</path/to/DirName> ~/data/ --recursive

7. meld版本查看