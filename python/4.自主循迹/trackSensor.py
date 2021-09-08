#!/bin/usr/env python
# +-----------------------------+
# |      循迹传感器
# | - 引脚说明：
# | 左1 左2 右1 右2
# | 3   5   4   18
# | - 功能说明：
# | 返回循迹传感器采集的信息
# +-----------------------------+

####! 传感器说明 ####
# 检测到黑线时循迹模块相应的指示灯亮，端口电平为LOW
# 未检测到黑线时循迹模块相应的指示灯灭，端口电平为HIGH

####! 引用需要使用的模块 ####
# +-----------------------------+
import RPi.GPIO as GPIO
import time

# 前期工作
# 指定GPIO的编码方式, 这里使用BCM编码方式。
# 具体信息参考 https://pinout.xyz/pinout/5v_power
GPIO.setmode(GPIO.BCM)

# (非必需)关闭警告信息
GPIO.setwarnings(False)

####! 变量定义 ####
# +----------------------------+
TrackSensorLeft1 = 3  # 左1
TrackSensorLeft2 = 5  # 左2
TrackSensorRight1 = 4  # 右1
TrackSensorRight2 = 18  # 右2


####! 初始化模块 ####
# +----------------------------+
# 初始化传感器引脚
def init_sensor():
    '''
    初始化循迹传感器。
    '''
    GPIO.setup(TrackSensorLeft1, GPIO.IN)
    GPIO.setup(TrackSensorLeft2, GPIO.IN)
    GPIO.setup(TrackSensorRight1, GPIO.IN)
    GPIO.setup(TrackSensorRight2, GPIO.IN)

####! 需要的功能封装成函数 ####
# +----------------------------+


def get_track_sensor_state():
    '''
    获取当前传感器状态。
    '''
    leftState1 = GPIO.input(TrackSensorLeft1)
    leftState2 = GPIO.input(TrackSensorLeft2)
    rightState1 = GPIO.input(TrackSensorRight1)
    rightState2 = GPIO.input(TrackSensorRight2)
    # 将结果写成一个元组返回给调用函数的地方
    return (leftState1, leftState2, rightState1, rightState2)


####! 测试 ####
if __name__ == '__main__':
    # 初始化
    init_sensor()
    # 获取状态
    state = get_track_sensor_state()
    print(state)
