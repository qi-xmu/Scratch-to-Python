#!/bin/usr/env python
# +-----------------------------+
# |        自主循迹
# | - 引脚说明：
# | 左1 左2 右1 右2
# | 3   5   4   18
# | - 功能说明：
# | 实现小车循迹。
# +-----------------------------+

####! 引用需要使用的模块 ####
# +-----------------------------+
# 引用系统自带的模块
import time
# 引用自己定义的模块
import motor
import trackSensor

#####! 在进入正常状态前初始化各个模块 ####
motor.motor_init()  # 初始化电机
trackSensor.init_sensor()  # 初始化循迹传感器

# 设置一些参数，方便调参
speed = 30  # 速度

ldtime = 0.05  # 小转弯延时时间
dtime = 0.08  # 转弯延时时间
bdtime = 0.1  # 大转弯延时时间

####! 进入正常的循迹逻辑 ####
# 逻辑梳理
# 获取传感器状态 --> 根据传感器状态决定小车的运动情况 --> 前进/左转/右转
# --> 获取传感器状态 --> ...(进入循环)
while True:
    # 首先获取传感器状态 将结果存入 state
    state = trackSensor.get_track_sensor_state()

    # 检测到黑线时循迹模块相应的指示灯亮，端口电平为LOW
    # 未检测到黑线时循迹模块相应的指示灯灭，端口电平为HIGH

    # 对 state 状态进行分类判断处理
    # 四路循迹引脚电平状态
    #  0 0 X 0
    #  1 0 X 0
    #  0 1 X 0
    # 以上6种电平状态时 小车右转
    if (state[0] == 0 or state[1] == 0) and (state[3] == 0):
        motor.turnRight(delay_time=dtime, duty=speed)
    # 0 X 0 0
    # 0 X 0 1
    # 0 X 1 0
    # 以上6种电平状态时 小车左转
    elif (state[2] == 0 or state[3] == 0) and (state[0] == 0):
        motor.turnLeft(delay_time=dtime, duty=speed)

    # 四路循迹引脚电平状态
    # 0 X X X
    # 最左边检测到 小车转弯时间可以适当变大 小车左转
    elif state[0] == 0:
        motor.turnLeft(delay_time=bdtime, duty=speed)
    # X X X 0
    # 最右边检测到 小车转弯时间可以适当变大 小车右转
    elif state[3] == 0:
        motor.turnRight(delay_time=bdtime, duty=speed)

    # 四路循迹引脚电平状态
    # X 0 1 X
    # 处理左小弯
    elif state[1] == 0 and state[2] == 1:
        motor.turnLeft(delay_time=ldtime, duty=speed)
    # X 1 0 X
    # 处理右小弯
    elif state[1] == 1 and state[2] == 0:
        motor.turnRight(delay_time=ldtime, duty=speed)

    # 四路循迹引脚电平状态
    # X 0 0 X
    # 处理直线
    elif state[1] == 0 and state[2] == 0:
        motor.forward(delay_time=dtime, duty=speed)

    # 当为1 1 1 1时小车保持上一个小车运行状态
