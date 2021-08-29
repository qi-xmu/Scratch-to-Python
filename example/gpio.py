#! /usr/bin/python

# +-----------------------------+
# |      树莓派GPIO使用说明       |
# +-----------------------------+

# Coded by Qi

# ! 参考文章
# https://shumeipai.nxez.com/2016/09/28/rpi-gpio-module-basics.html

# 引入GPIO模块
import RPi.GPIO as GPIO

# 指定GPIO的编码方式, 这里使用BCM编码方式。
# 具体信息参考 https://pinout.xyz/pinout/5v_power
GPIO.setmode(GPIO.BCM)

# (非必需)关闭警告信息
GPIO.setwarnings(False)

# ! 下面介绍GPIO的基本操作（channel 可以自行修改，这里选的的是 GPIO2）
# 设置引脚的状态 输入/输出
channel = 2
GPIO.setup(channel, GPIO.OUT)  # 输出模式
# or
GPIO.setup(channel, GPIO.IN)  # 输入模式

# 在输入模式中 可以设置引脚的上拉或者下拉（可以理解为输入状态的初始默认状态 上拉对应高电平）
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 设置上拉，初始状态为高电平
# or
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # 设置上拉，初始状态为低电平

# 输出模式 可以设置引脚的电平状态 高电平/低电平
GPIO.output(channel, GPIO.HIGH)  # 设为高电平
# or
GPIO.output(channel, GPIO.LOW)  # 设为低电平

# 输入模式 可以读取引脚的状态值 高电平/低电平/模拟值
GPIO.input(channel)  # 读取引脚状态 得到0/1 对应低/高电平


# ! 进阶 设置回调函数
# 下面为回调函数
def callback_func():
    print("channel 2 is Rising!")


# 下面的代码不会阻塞程序运行
# 当channel的状态从低电平变化成高电平，就会执行传入的callback_func函数
# callback_func可以自定义，也可以自己更改名称。
# bouncetime为了避免按键的机械振动带来的错误信号
GPIO.add_event_detect(channel,
                      GPIO.RISING,
                      callback=callback_func,
                      bouncetime=200)

# ! 使用完GPIO资源，在程序结束前释放资源
GPIO.cleanup()
