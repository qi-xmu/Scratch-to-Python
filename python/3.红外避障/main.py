#! /usr/bin/python

# +-----------------------------+
# |        红外避障
# | - 引脚说明：
# | 左侧：12 右侧：17
# | - 功能说明：
# | 实现小车避障。
# +-----------------------------+


#! 红外避障原理
# 红外传感器可以根据距离的远近，返回高低电平。
# 障碍物较远，返回高电平
# 障碍物较近，返回低电平
# 可以通过调节旋钮，调节传感器的灵敏度。

# Coded by Qi

####! 引用需要使用的模块 ####
# +----------------------------+

import RPi.GPIO as GPIO
from time import sleep

####! 引用文件 ####
# 控制电机，直接引用motor.py里的函数进行控制即可（注意motor.py和main.py在相同目录下）
import motor


# 指定GPIO的编码方式, 这里使用BCM编码方式。
# 具体信息参考 https://pinout.xyz/pinout/5v_power
GPIO.setmode(GPIO.BCM)
# (非必需)关闭警告信息
GPIO.setwarnings(False)

####! 变量定义 ####
# +----------------------------+
# 定义引脚
leftSensor = 12
rightSensor = 17


####! 初始化引脚 ####
# +----------------------------+
def init_sensor():
    '''
    初始化红外传感器。设置为输入模式。
    '''
    GPIO.setup(leftSensor, GPIO.IN)
    GPIO.setup(rightSensor, GPIO.IN)


####! 避障逻辑 ####
# +----------------------------+
# 首先初始化传感器和电机
init_sensor()
# motor.py里的函数，引用后可以直接使用
motor.init()

# 主循环
while True:
    leftState = GPIO.input(leftSensor)  # 获取左侧传感器的状态
    rightState = GPIO.input(rightSensor)  # 获取右侧传感器的状态

    # 逻辑分支 if elif(else if的合体) else
    if leftState == GPIO.HIGH and rightState == GPIO.HIGH:
        # 没有障碍物 前进
        motor.forward()
    elif leftState == GPIO.LOW and rightState == GPIO.HIGH:
        # 左侧有障碍物 右转
        motor.right()
    elif leftState == GPIO.HIGH and rightState == GPIO.LOW:
        # 右侧有障碍物 左转
        motor.left()
    else:
        # 两侧都有障碍物 先后退再右转
        motor.backward(1)
        motor.right()
