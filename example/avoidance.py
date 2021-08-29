#! /usr/bin/python

# +-----------------------------+
# |        超声波避障            |
# | - 引脚说明：                 |
# |                             |
# | 超声波 20   21   16          |
# | - 功能说明：                 |
# | 实现前进 后退 左转 右转。      |
# +-----------------------------+

# ! 超声波测距原理
# 超声波一共有四个引脚，分别控制Trig Echo VCC GND
# VCC GND 分别连接电源正极和地线。
# 当需要测距时， 我们控制Trig引脚，产生一个至少10us的高电平脉冲信号（相当于发出声波，遇到障碍物会反射回来）
# 然后监控Echo引脚的返回信号，Echo引脚原本是低电平，它会先拉高再拉低，其中 高电平持续时间 就是传感器从发出信号到接收到信号的时间。
# 根据声速，可以测量出障碍物到超声波的距离。
# 一般使用的超声波模块的测量范围为 2mm~2000mm

# Coded by Qi


####! 引用需要使用的模块 ####
# +------------------------------------------------+
import RPi.GPIO as GPIO
from time import time, sleep


####! 变量定义 ####
# +------------------------------------------------+
# 定义引脚 （后面修改）
trig = None
echo = None


####! 函数定义 ####
# +------------------------------------------------+

# 首先初始化引脚 写成一个函数
def init_distance():
    '''
    初始化超声波使用的GPIO。
    '''
    # 指定GPIO的编码方式, 这里使用BCM编码方式。
    # 具体信息参考 https://pinout.xyz/pinout/5v_power
    GPIO.setmode(GPIO.BCM)

    # (非必需)关闭警告信息
    GPIO.setwarnings(False)

    # 信号发送端 设置为输出
    GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)
    # 信号接收端 设置为输入
    GPIO.setup(echo, GPIO.IN)


def delay_ms(millisecond):
    '''
    延时函数 单位：毫秒(ms)
    '''
    sleep(millisecond / 1000)


def delay_us(microsecond):
    '''
    延时函数 单位：微秒(us)
    '''
    sleep(microsecond / 1000000)


def get_distance():
    '''
    获得障碍物到传感器的距离。
    主要分为三步：发射信号 接收信号 计算距离。
    '''
    # 第一步 发射测距信号
    GPIO.output(trig, GPIO.LOW)
    delay_us(2)  # 延时2us
    GPIO.output(trig, GPIO.HIGH)
    delay_us(10)  # 延时10us
    GPIO.output(trig, GPIO.LOW)

    # 第二步 接收脉冲信号
    start_time = time()  # 记录低电平结束时间
    stop_time = time()  # 记录高电平结束时间
    while GPIO.input(echo) == GPIO.LOW:
        start_time = time()
    while GPIO.input(echo) == GPIO.HIGH:
        end_time = time()
    pulse_time = end_time - start_time  # 脉冲时间

    # 第三步 计算测量距离
    # 公式：(pulse_time * 34300(声速34300cm/s)) / 2 (往返) (单位：cm)
    distance = (pulse_time * 34300) / 2

    # 函数返回值为测量的距离
    return distance


if __name__ == '__main__':
    while True:
        print(f"Distance now is {get_distance()}cm")
        delay_ms(1000)  # 延时1s
