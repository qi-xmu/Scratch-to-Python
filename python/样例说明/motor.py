#! /usr/bin/python

# +-----------------------------+
# |        电机控制              |
# | - 引脚说明：                 |
# |      方向1 方向2 速度         |
# | 左电机 20   21   16          |
# | 右电机 19   26   13          |
# | - 功能说明：                 |
# | 实现前进，后退，左转，右转。   |
# +-----------------------------+

# Coded by Qi

####! 引用需要使用的模块 ####
# +------------------------------------------------+
import RPi.GPIO as GPIO
import time

# 前期工作
# 指定GPIO的编码方式, 这里使用BCM编码方式。
# 具体信息参考 https://pinout.xyz/pinout/5v_power
GPIO.setmode(GPIO.BCM)

# (非必需)关闭警告信息
GPIO.setwarnings(False)

####! 变量定义 ####
# +------------------------------------------------+
# 左电机
AIN1 = 20
AIN2 = 21  # 这两个用于控制电机转向 正转/反转
ENA = 16  # 控制电机转速
# 右电机
BIN1 = 19
BIN2 = 26  # 这两个用于控制电机转向 正转/反转
ENB = 13  # 控制电机转速

####! 函数定义说明 ####
# +------------------------------------------------+
# 格式如下： (注意冒号不能少)
# def function_name(params):
#   do_something()

# python中函数不能为空，若要为空，需要使用pass， 如下
# def example():
#   pass


def motor_init():
    '''
    初始化电机。
    '''
    # 设置引脚为输出状态。
    GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)  # 初始状态为低电平
    GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BIN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BIN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)  # 初始状态为高电平
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.HIGH)

    # 关键字 "global" 将变量设置为全局变量 若没有声明 pwm_ENA/B的有效作用范围只能在这个函数内
    global pwm_ENA
    global pwm_ENB
    # 电机的速度通过PWM方式控制 设置频率为2000Hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    # 设置占空比暂时为0
    duty = 0
    pwm_ENA.start(duty)
    pwm_ENB.start(duty)


def forward(delay_time=0, duty=50):
    '''
    小车前进。
    delay_time: 前进的时间。单位：秒。默认值：0。
    duty: 占空比，反映速度快慢，默认值：50。
    '''
    # 设置电机为正转
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    # 设置占空比 0~100 占空比越大速度越快
    pwm_ENA.ChangeDutyCycle(duty)
    pwm_ENB.ChangeDutyCycle(duty)
    time.sleep(delay_time)


def backward(delay_time=0, duty=50):
    '''
    小车后退。
    delay_time: 后退的时间。单位：秒。默认值：0。
    duty: 占空比，反映速度快慢，默认值：50。
    '''
    # 设置电机为反转
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    # 设置占空比 0~100 占空比越大速度越快
    pwm_ENA.ChangeDutyCycle(duty)
    pwm_ENB.ChangeDutyCycle(duty)
    time.sleep(delay_time)


def turnLeft(delay_time=0, duty=50):
    '''
    小车左转。
    delay_time: 左转的时间。单位：秒。默认值：0。
    duty: 占空比，反映速度快慢，默认值：50。
    '''
    # 设置电机为反转
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    # 设置占空比 0~100 占空比越大速度越快
    # pwm_ENA.ChangeDutyCycle(duty)
    pwm_ENB.ChangeDutyCycle(duty)
    time.sleep(delay_time)


def turnRight(delay_time=0, duty=50):
    '''
    小车右转。
    delay_time: 右转的时间。单位：秒。默认值：0。
    duty: 占空比，反映速度快慢，默认值：50。
    '''
    # 设置电机为反转
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)
    # 设置占空比 0~100 占空比越大速度越快
    pwm_ENA.ChangeDutyCycle(duty)
    # pwm_ENB.ChangeDutyCycle(duty)
    time.sleep(delay_time)


def stop(delay_time=0):
    '''
    让小车停下。
    delay_time: 停止时间。单位：秒。默认值：0。
    '''
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(0)
    pwm_ENB.ChangeDutyCycle(0)


####! 测试 ####
# +------------------------------------------------+

# 判断是否执行的是当前文件，若是则执行下面的代码。当从其他文件引用时，不执行下列代码。
if __name__ == '__main__':
    # 初始化电机
    motor_init()
    # 测试函数功能 占空比使用默认值为 50
    forward(3)  # 前进1s
    backward(3)  # 后退1s
    turnLeft(3)  # 左转1s
    turnRight(3)  # 右转1s
    stop()  # 停止
