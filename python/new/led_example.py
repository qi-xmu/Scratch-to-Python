import time
from module.LED import *

# 关于点灯的部分
led1 = LED(3)
# 点亮led
led1.turn_on()
# 熄灭
led1.turn_off()
# 设置亮度
led1.brightness(10)


# 实现亮灭5次
for i in range(5):
    led1.turn_on()
    time.sleep(1)
    led1.turn_off()
    time.sleep(1)

# 实现渐变灯效果
step = 1
liangdu = 0

for i in range(50000):
    liangdu += step
    if liangdu == 0 or liangdu == 100:
        step = - step
    led1.brightness(liangdu)
    time.sleep(0.01)


# 按键控制led
led2 = LED(4)
btn = Button(5)
btn.bind(led2)
