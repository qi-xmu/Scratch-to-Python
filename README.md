<<<<<<< HEAD
# 树莓派Scratch-to-Python
=======
# 树莓派巡线小车
>>>>>>> 117b0b6355801509379ddc6a08d2d203a80ca08c

## 项目目标

### 项目流程

- 制作树莓派镜像。（开发环境）
- led电灯程序。（变量，常量，表达式，赋值）
- 电机和小车控制。（函数）
- 小车走迷宫。（分支，循环）
- 小车自动避障。（判断）
- 巡线小车。（最终目标）

### 项目要求

- 使用scratch和python对比编程。

## 第一部分 树莓派入门



## 第二部分 led点灯程序

### 查询Raspberry Pi的引脚图

[WiringPi at Raspberry Pi GPIO Pinout](https://pinout.xyz/pinout/wiringpi)

<img src=".Instruction-media/image-20210827222937066.png" alt="image-20210827222937066" style="zoom:50%;" />

我们使用的引脚是`GPIO2 GPIO3`，其中 `GPIO2`接LED灯，`GPIO3`接按键。我们使用了一个和**回调函数**监控按键的发生，当回调的条件满足时，触发回调函数，执行回调函数内的代码。

## 第三部分 电机驱动

### 电机驱动原理

[第7章 用树莓派控制直流电机(L298N) - 简书 (jianshu.com)](https://www.jianshu.com/p/b970403a647f)

​		电机有专门的芯片控制，我们不需要去了解芯片的内在构造，只需要了解如何使用这种芯片。电机的输出端一般时接好的。电机的输入段一共有六个（`ENA, ENB, IN1, IN2, IN3, IN4`），每三个控制一个电机（或者说同边的电机）。下表是其中一组电机控制的真值表，另一组为（`ENB, IN3, IN4`）。同过下表，可知。

![image-20210830194032885](.Instruction-media/image-20210830194032885.png)

控制电机主要包含两部分：**转向**和**转速**。

#### 转向

`IN1 IN2`（或者`IN3 IN4`）用于控制电机的转向（正转/反转）。我们需要前进或者后退时，只需要将`IN1 IN2`其中一个设置为高电平。（具体哪一个是前进要结合电机的安装方式，正转不一定是前进）。需要停止时，只需要将`IN1 IN2`同时设置为低电平。

#### 转速

`ENA`（或者`ENB`）用于控制电机的转速，相当于控制小车速度。当其设置为1时，电机全速旋转。一般来说，我们不会让电机全速（转速太快），所以我们通过**PWM**调节电机的速度。PWM的原理不必深究，我们只需要知道怎么通过PWM控制转速。PWM有两个重要参数，频率和占空比。频率这里我们使用默认值2000（频率大小不影响电机速度），而占空比（1~100）和电机速度成正比，我们只需要调节占空比就可以实现对电机速度的控制。

## 第四部分 超声波避障

[(4条消息) 超声波测距_liudongdong_jlu-CSDN博客_超声波测距](https://blog.csdn.net/liudongdong19/article/details/81005930) 

### 超声波避障原理

