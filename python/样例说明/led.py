#! /usr/bin/python

# +-----------------------------+
# |         LED电灯程序          |
# | GPIO2 接按键 | GPIO3  接LED灯|
# | 功能说明：                   |
# | 按键切换LED灯状态。           |
# +-----------------------------+

# Coded by Qi

####! 使用GPIO模块需要的工作 ####
# +------------------------------------------------+
# 引入GPIO模块
import RPi.GPIO as GPIO

# 指定GPIO的编码方式, 这里使用BCM编码方式。
# 具体信息参考 https://pinout.xyz/pinout/5v_power
GPIO.setmode(GPIO.BCM)

# (非必需)关闭警告信息
GPIO.setwarnings(False)

####! 变量定义 ####
# +------------------------------------------------+
# "=" 表示赋值。用法： 变量名 = 数值
# 选择需要控制的GPIO引脚
# button引引脚，按键一边接GPIO2，一边接5v。
btn_pin = 2

# led引脚接LED灯的正极, 另一个引脚接地线(GND)。
led_pin = 3

####! 初始化所使用的GPIO ####
# +------------------------------------------------+
# 因为要控制LED灯，所以led_pin设置为输出模式
GPIO.setup(led_pin, GPIO.OUT)  # 输出模式

# 检测按键的状态，当按键引脚的状态发生改变时，该改变灯的状态。
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # 输入模式, 并设置下拉

# 先设置LED灯的状态为灭
GPIO.output(led_pin, GPIO.LOW)


####! 实现按键控制LED功能 ####
# +------------------------------------------------+
# 设置按键的回调函数，当检测到按键按下时执行
def pressed():
    # 读取当前LED的状态
    state = GPIO.input(led_pin)
    # 将LED的状态取反 "not"关键字表示将state取反
    GPIO.output(led_pin, not state)


# 设置监控 注意这里的回调函数不需要括号
GPIO.add_event_detect(btn_pin, GPIO.RISING, callback=pressed, bouncetime=200)
