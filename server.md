1  lspci -nn | grep -i net
    2  uname -r
    3  sudo apt update
    4  sudo apt install gcc make build-essential git linux-headers-$(uname -r)
    5  wget https://raw.githubusercontent.com/pimlie/ubuntu-mainline-kernel.sh/master/ubuntu-mainline-kernel.sh
    6  sudo install ubuntu-mainline-kernel.sh /usr/local/bin/
    7  ubuntu-mainline-kernel.sh -i
    8  sudo ubuntu-mainline-kernel.sh -i
    9  sudo reboot now
   10  ubuntu-mainline-kernel.sh -u
   11  sudo ubuntu-mainline-kernel.sh -u
   12  sudo reboot now
   13  sudo modprobe mt76
   14  sudo service network-manager restart
   15  sudo modprobe mt76-sdio
   16  sudo service network-manager restart
   17  sudo reboot now
   18  sudo apt install linux-firmware
   19  sudo ubuntu-mainline-kernel.sh -i 5.12.11
   20  sudo reboot now
   21  grub-rescue
   22  sudo ubuntu-mainline-kernel.sh -u
   23  sudo grub-rescue
   24  sudo ubuntu-mainline-kernel.sh
   25  sudo ubuntu-mainline-kernel.sh -u
   26  sudo ubuntu-mainline-kernel.sh -i
   27  sudo reboot now
   28  sudo apt get install -f
   29  sudo apt-get install -f
   30  sudo reboot now
   31  locale
   32  sudo apt update && sudo apt install curl gnupg2 lsb-release
   33  sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
   34  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
   35  sudo sed -i -e 's/ubuntu .* main/ubuntu focal main/g' /etc/apt/sources.list.d/ros2.list
   36  sudo apt update
   37  sudo apt install ros-foxy-desktop
   38  source /opt/ros/foxy/setup.bash
   39  sudo apt uninstall ros-foxy-desktop
   40  sudo apt remove ros-foxy-desktop
   41  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
   42  sudo apt-get install mesa-utils
   43  glxgears
   44  mkdir -p ~/ros2_foxy
   45  cd ros2_foxy/
   46  tar xf ~/Downloads/ros2-foxy-20211013-linux-focal-amd64.tar.bz2 
   47  ls
   48  sudo apt update
   49  sudo apt install -y python3-rosdep
   50  sudo rosdep init
   51  rosdep update
   52  rosdep install --from-paths ~/ros2_foxy/ros2-linux/share --ignore-src -y --skip-keys "cyclonedds fastcdr fastrtps rti-connext-dds-5.3.1 urdfdom_headers"
   53  pip3 install -U argcomplete
   54  sudo apt install -y libpython3-dev python3-pip
   55  pip3 install -U argcomplete
   56  . ~/ros2_foxy/ros2-linux/setup.bash
   57  ros2 run demo_nodes_cpp listener
   58  rviz2
   59  curl -sSL http://get.gazebosim.org | sh
   60  gazebo
   61  rviz2
   62  . ~/ros2_foxy/ros2-linux/setup.bash
   63  echo $RMW_IMPLEMENTATION
   64  sudo apt-get install ros-foxy-rmw-connext-cpp
   65  . ~/ros2_foxy/ros2-linux/setup.bash
   66  git clone -b ros2 https://github.com/slamtec/rplidar_ros.git
   67  cd rplidar_ros/
   68  ls
   69  colcon build --symlink-install
   70  sudo apt install python3-colcon-common-extensions
   71  ls
   72  cd src/
   73  ls
   74  cd -
   75  colcon build --symlink-install
   76  . ~/ros2_foxy/ros2-linux/setup.bash
   77  cd rplidar_ros/
   78  ls
   79  colcon build --symlink-install
   80  source ./install/setup.bash 
   81  ros2 launch rplidar_ros2 view_rplidar_launch.py
   82  ls -l /dev |grep ttyUSB
   83  sudo chmod 666 /dev/ttyUSB0
   84  ls -l /dev |grep ttyUSB
   85  ros2 launch rplidar_ros2 view_rplidar_launch.py
   86  ls -l /dev |grep ttyUSB
   87  sudo chmod 666 /dev/ttyUSB0
   88  sudo chmod 666 /dev/ttyUSB1
   89  ros2 launch rplidar_ros2 view_rplidar_launch.py
   90  sudo chmod 666 /dev/ttyUSB1
   91  sudo chmod 666 /dev/ttyUSB0
   92  ls -l /dev |grep ttyUSB
   93  . ~/ros2_foxy/ros2-linux/setup.bash
   94  cd rplidar_ros/
   95  source ./install/setup.bash 
   96  ros2 launch rplidar_ros2 view_rplidar_launch.py
   97  ls -l /dev |grep ttyUSB
   98  sudo chmod 666 /dev/ttyUSB0
   99  ros2 launch rplidar_ros2 view_rplidar_launch.py
  100  history
  101  . ~/ros2_foxy/ros2-linux/setup.bash
  102  ros2 topic list
  103  cd rplidar_ros/
  104  source ./install/setup.bash 
  105  ros2 topic list
  106  ros2 run demo_nodes_cpp talker
  107  ros2 topic list
  108  sudo apt update
  109  ros2 topic list
  110  ros2 launch rplidar_ros2 view_rplidar_launch.py
  111  sudo apt update
  112  sudo apt upgrade
  113  . ~/ros2_foxy/ros2-linux/setup.bash
  114  ros2 topic list
  115  cd rplidar_ros/
  116  source ./install/setup.bash 
  117  ros2 launch rplidar_ros2 view_rplidar_launch.py
  118  ros2 topic list
  119  ros2 run rqt_image_view rqt_image_view
  120  sudo apt install ros-foxy-rqt*
  121  ros2 run rqt_image_view rqt_image_view
  122  rqt
  123  rviz2
  124  sudo apt-get ros-foxy-rqt-image-view
  125  sudo apt-get install ros-foxy-rqt-image-view
  126  . ~/ros2_foxy/ros2-linux/setup.bash
  127  ros2 run rqt_image_view rqt_image_view
  128  source /opt/ros/foxy/setup.bash
  129  ros2 run rqt_image_view rqt_image_view
  130  sudo o apt install ros-foxy-image-transport-plugins 
  131  sudo apt install ros-foxy-image-transport-plugins 
  132  source /opt/ros/foxy/setup.bash
  133  ros2 run rqt_image_view rqt_image_view
  134  ros2 topic list
  135  ros2 run rqt_image_view rqt_image_view
  136  source /opt/ros/foxy/setup.bash
  137  . ~/ros2_foxy/ros2-linux/setup.bash
  138  ros2 run rqt_image_view rqt_image_view
  139  ros2 run rqt_image_view rqt_image_view --ros-args -p _image_transport:=compressed
  140  source /opt/ros/foxy/setup.bash
  141  . ~/ros2_foxy/ros2-linux/setup.bash
  142  ls
  143  ros2 topic list
  144  ros2 run rqt_image_view rqt_image_view --ros-args -p /image_raw -p _image_transport:=compressed
  145  ros2 run rqt_image_view rqt_image_view  _image_transport:=compressed
  146  ros2 run rqt_image_view rqt_image_view
  147  ;s
  148  ls
  149  cd ros2_foxy/
  150  ls
  151  ls ros2-linux/
  152  cd
  153  ls
  154  ros2 topic list
  155  ros2 run rqt_image_view rqt_image_view
  156  ssh ubuntu@192.168.1.136
  157  printenv | grep -i ROS
  158  source /opt/ros/foxy/setup.bash
  159  . ~/ros2_foxy/ros2-linux/setup.bash
  160  ros2 run rqt_image_view rqt_image_view
  161  rviz2
  162  . ~/ros2_foxy/ros2-linux/setup.bash
  163  rviz2
  164  ls
  165  . ~/ros2_foxy/ros2-linux/setup.bash
  166  ls
  167  ls ros2_foxy/
  168  sudo apt update && sudo apt install curl gnupg2 lsb-release
  169  rm -rf ros2_foxy/
  170  mkdir -p ~/ros2_foxy
  171  cd ~/ros2_foxy
  172  tar xf ~/Downloads/ros2-package-linux-x86_64.tar.bz2
  173  tar xf ~/Downloads/ros2-foxy-20211013-linux-focal-amd64
  174  tar xf ~/Downloads/ros2-foxy-20211013-linux-focal-amd64.tar.bz2 
  175  ls
  176  sudo apt update
  177  sudo apt install -y python3-rosdep
  178  sudo rosdep init
  179  rm /etc/ros/rosdep/sources.list.d/20-default.list
  180  sudo rm /etc/ros/rosdep/sources.list.d/20-default.list
  181  sudo apt install -y python3-rosdep
  182  sudo rosdep init
  183  rosdep update
  184  rosdep install --from-paths ~/ros2_foxy/ros2-linux/share --ignore-src -y --skip-keys "cyclonedds fastcdr fastrtps rti-connext-dds-5.3.1 urdfdom_headers"
  185  sudo apt install -y libpython3-dev python3-pip
  186  . ~/ros2_foxy/ros2-linux/setup.bash
  187  printenv | grep -i ROS
  188  history
  189  ros2 run rqt_image_view rqt_image_view
  190  ls
  191  cd
  192  ls
  193  mkdir -p ros2_ws/src && cd ros2_ws/src
  194  ros2 run image_tools cam2image
  195  sudo apt-get ros-foxy-rqt-image-view
  196  sudo apt-get install ros-foxy-rqt-image-view
  197  ros2 run rqt_image_view rqt_image_view
  198  cd
  199  ros2 run rqt_image_view rqt_image_view
  200  sudo apt-get remove ros-foxy-rqt-image-view
  201  sudo apt-get install ros-foxy-rqt-image-view
  202  ros2 run rqt_image_view rqt_image_view
  203  . ~/ros2_foxy/ros2-linux/setup.bash
  204  ros2 run rqt_image_view rqt_image_view
  205  ls ~/Downloads/
  206  ssh ubuntu@192.168.1.136
  207  cd ..
  208  ls
  209  source /opt/ros/foxy/setup.bash
  210  . ~/ros2_foxy/ros2-linux/setup.bash
  211  ros2 run rqt_image_view rqt_image_view
  212  . ~/ros2_foxy/ros2-linux/setup.bash
  213  ros2 run rqt_image_view rqt_image_view
  214  ros2 topic list
  215  source /opt/ros/foxy/setup.bash
  216  . ~/ros2_foxy/ros2-linux/setup.bash
  217  ros2 run rqt_image_view rqt_image_view
  218  ros2 run rqt_image_view rqt_image_view  _image_transport:=compressed
  219  ros2 run rqt_image_view rqt_image_view --ros-args --remap _image_transport:=compressed
  220  ssh ubuntu@192.168.1.136
  221  printenv | grep -i ROS
  222  . ~/ros2_foxy/install/local_setup.bash
  223  ls
  224  cd ros2_foxy/
  225  . ~/ros2_foxy/install/local_setup.bash
  226  ls 
  227  cd
  228  printenv | grep -i ROS
  229  which ros2
  230  ls /opt/ros/foxy/
  231  vcs -v
  232  sudo apt-get install vcs
  233  lsb_release -a
  234  sudo apt update && sudo apt install -y   build-essential   cmake   git   libbullet-dev   python3-colcon-common-extensions   python3-flake8   python3-pip   python3-pytest-cov   python3-rosdep   python3-setuptools   python3-vcstool   wget
  235  sudo apt autoremove
  236  rm -rf ros2_foxy/
  237  mkdir -p ~/ros2_foxy/src
  238  cd ros2_foxy/
  239  wget https://raw.githubusercontent.com/ros2/ros2/foxy/ros2.repos
  240  vcs import src < ros2.repos
  241  sudo rosdep init
  242  sudo rm /etc/ros/rosdep/sources.list.d/20-default.list
  243  sudo rosdep init
  244  rosdep update
  245  rosdep install --from-paths src --ignore-src -y --skip-keys "fastcdr rti-connext-dds-5.3.1 urdfdom_headers"
  246  ls
  247  ls src/
  248  cd ~/ros2_foxy/
  249  colcon build --symlink-install
  250  cd
  251  ssh ubuntu@192.168.1.136
  252  . ~/ros2_foxy/ros2-linux/setup.bash
  253  cd rplidar_ros/
  254  source ./install/setup.bash 
  255  ros2 launch rplidar_ros2 view_rplidar_launch.py
  256  ssh ubuntu@192.168.1.136
  257  cd ros2_ws/
  258  . ~/ros2_foxy/ros2-linux/setup.bash
  259  source /opt/ros/foxy/setup.bash
  260  ros2 run rqt_image_view rqt_image_view --ros-args --remap _image_transport:=compressed
  261  ssh ubuntu@192.168.1.136
  262  cd ..
  263  ls
  264  cd rplidar_ros/
  265  . ~/ros2_foxy/ros2-linux/setup.bash
  266  ros2 launch rplidar_ros2 view_rplidar_launch.py
  267  source ./install/setup.bash 
  268  ros2 launch rplidar_ros2 view_rplidar_launch.py
  269  ssh ubuntu@192.168.1.136
  270  history
mattsroufe@ubuntu-laptop:~$ 

