1 上手教程
==========

2 升级固件
==========

3 Linux开发
===========

3.1 编译Linux
-------------

3.1.1 搭建编译环境
~~~~~~~~~~~~~~~~~~

-  操作系统：ubuntu18.04
-  主机环境：64位CPU 16GB物理内存+交换内存 250GB空闲磁盘空间

软件包安装参考

.. code:: bash

   sudo apt-get install qemu-user-static binfmt-support debootstrap -y

3.1.2 获取SDK
~~~~~~~~~~~~~

SDK通过销售获取，笔者这里获取SDK包为A33LinuxSDK_20240222.tar.gz，新建开发目录~/work/a33，并解压SDK。
执行以下命令：

.. code:: bash

   mkdir ~/work/a33 -p
   tar -xzvf A33LinuxSDK_20240222.tar.gz -C ~/work/a33
   cd ~/work/a33/A33LinuxSDK_20240222/

3.1.3 编译uboot
~~~~~~~~~~~~~~~

执行以下命令：

.. code:: bash

   cd ~/work/a33/A33LinuxSDK_20240222/brandy/u-boot-2011.09/
   make distclean
   make sun8iw5p1
   make -j8

编译完成如下打印：

::

   /home/jonlee/work/a33/A33LinuxSDK_20240222/brandy/gcc-linaro/bin/../lib/gcc/arm-linux-gnueabi/4.6.3 -lgcc -Map u-boot.map -o u-boot
   /home/jonlee/work/a33/A33LinuxSDK_20240222/brandy/u-boot-2011.09/../gcc-linaro/bin/arm-linux-gnueabi-objcopy -O srec u-boot u-boot.srec
   /home/jonlee/work/a33/A33LinuxSDK_20240222/brandy/u-boot-2011.09/../gcc-linaro/bin/arm-linux-gnueabi-objcopy --gap-fill=0xff -O binary u-boot u-boot.bin
   'u-boot-sun8iw5p1.bin' -> '/home/jonlee/work/a33/A33LinuxSDK_20240222/brandy/u-boot-2011.09/../../tools/pack/chips/sun8iw5p1/bin/u-boot-sun8iw5p1.bin'

3.1.4 编译kernel
~~~~~~~~~~~~~~~~

执行以下配置命令：

.. code:: bash

   cd ~/work/a33/A33LinuxSDK_20240222/
   cp linux-3.4/a33_alpaca_defconfig linux-3.4/.config
   ./build.sh config
   Welcome to mkscript setup progress
   All available chips:
      0. sun8iw5p1
   Choice: 0
   All available platforms:
      0. android
      1. dragonboard
      2. linux
   Choice: 1
   All available kernel:
      0. linux-3.4
   Choice: 0
   All available boards:
      0. alpaca
      1. evb
      2. maple
      3. redwood
      4. y2
      5. y3
   Choice: 0

再执行如下命令编译：

.. code:: bash

   ./build.sh

编译完成如下打印：

::

   regenerate rootfs cpio
   8772 blocks
   9473 blocks
   build_ramfs
   Copy boot.img to output directory ...
   INFO: build kernel OK.
   INFO: build rootfs ...
   Regenerating dragonboard Rootfs...
   generating rootfs...
   success in generating rootfs
   Build at: 2024年 05月 07日 星期二 15:32:41 CST
   INFO: build rootfs OK.
   INFO: ----------------------------------------
   INFO: build lichee OK.
   INFO: ----------------------------------------

3.1.5 编译文件系统
~~~~~~~~~~~~~~~~~~

文件系统已预置进SDK，不需要再次编译。 ### 3.1.6 打包固件
执行以下命令打包固件：

::

   ./build.sh pack

打包完成如下打印：

::

   Venv.fex Len: 0x4
   boot.fex Len: 0xc3f800
   Vboot.fex Len: 0x4
   rootfs.fex Len: 0x40000000
   Vrootfs.fex Len: 0x4
   BuildImg 0
   Dragon execute image.cfg SUCCESS !
   ----------image is at----------

   /home/jonlee/work/a33/A33LinuxSDK_20240222/tools/pack/sun8iw5p1_dragonboard_alpaca.img                                                                                    
                                                                                                                                                                             
   pack finish

sun8iw5p1_dragonboard_alpaca.img即为编译后的烧录固件，使用烧录工具即可烧录至主板。
### 3.1.6 支持QT ### 3.1.7 支持LVGL ## 3.2 Linux接口测试 ### 3.2.1
GPIO使用 ### 3.2.2 UART使用 ### 3.2.3 SPI使用 ### 3.2.4 Camera使用 ###
3.2.5 RTC使用 ### 3.2.6 Watchdog使用 ### 3.2.7 WIFI使用 ### 3.2.8
Ethernet使用 ### 3.2.9 BT使用 ### 3.2.10 KEY使用 # 4 Android开发 # 5
开发记录 ## 5.1 显示支持TTL接口RGB分辨率 ## 5.2 显示支持LVDS接口分辨率
## 5.3 显示支持86屏幕接口分辨率
