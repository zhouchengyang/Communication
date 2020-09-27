# SenseTime CheatSheet
* AWS设置

  aws configure --profile ad_system_common
  AWS Access Key ID [None]:O5B34FE51MMZRZGEY1Z5
  AWS Secret Access Key [None]:Xh6hOX5xnZ6BrsNnCcCt8NzNCbWeCSYwtABErKJ6

* Docker设置

  创建docker容器

  下载docker镜像docker pull balabala或者执行system/scripts/docker/pull_docker_image.bash

  新建自己的docker bash system/scripts/docker/build_owner_docker.sh --source-image='core.harbor.domain/senseauto/developer:latest' --target-image=my_image:from_developer

  新建docker container ./system/scripts/docker/docker_run.sh -m ~/docker_ws/repo_pro/ -d ~ -i my_image:from_developer -l /usr/local/senseauto_local

  docker exec -it 9d2580c620cb bash

* 代码和远程同步
  cd ~/docker_ws/repo_pro/senseauto && ./system/scripts/repo/sync.sh

  git push origin HEAD:refs/for/master%topic=A
  
* commit规范

```
AUTODRIVE-2428 repair speed too high bug
 
* Speed is too high, which is dangers.
* Took Throttle as Brake.
* Correctly handle throttle and brake.
```
* 下载topic
  repo download-topic AUTODRIVE-`0000_Create_Branch_MyBranch`
  repo sync -d -j4 

* 下载二进制包

  ./system/scripts/binary_release/download.py interaction -i prebuild/ --topic AUTODRIVE-5632_fix_bug_of_fallback

* 启动plotjuggler
  rosrun plotjuggler PlotJuggler

* 输出日志文件:
  vim /tmp/ros_decision_planning_node.txt 

* 启动hmi的polygon显示

  visualier.launch display_in_polygon = true

* 场景编辑器
  cd ~/ws/repo_pro/senseauto/modules/simulator/tools/scenario_editor/ && ./auto_start.sh
  打开locahost:8085

* 第三方库编译流程

  本地编译：进入docker，找到mpc_lon_code_generator/code_generation.sh

  远程编译：ssh nvidia@10.151.176.84 找到zhouchengyang，然后进入code_generation.sh
  
* 脱域：i have no name找it

* Kazam
  https://ywnz.com/linuxrj/2762.html

  super+ctrl+q 退出

  super+ctrl+r 开始录制

  super+ctrl+f 退出录制

  super+ctrl+p 暂停

  ctrl+alt+a 截图需要配置

* aws操作

  aws 配置：aws configure 输入邮件中的key和id

  aws 列出：aws s3 ls s3://Field_Test_Data/master/segment_data/2020_xx_xx/CN017/DPC/take_over/

  aws 列出：aws s3 ls s3://Field_Test_Data/master/raw_data/

  aws 下载目录：aws s3 cp s3://Field_Test_Data/</path/to/DirName> ~/data/ --recursive

