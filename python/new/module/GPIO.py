import RPi.GPIO as GPIO
import time

# 前期工作
# 指定GPIO的编码方式, 这里使用BCM编码方式。
# 具体信息参考 https://pinout.xyz/pinout/5v_power
GPIO.setmode(GPIO.BCM)

# (非必需)关闭警告信息
GPIO.setwarnings(False)
