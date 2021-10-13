from time import sleep
from module import Ultrasound


# 1 定义一个对象
us = Ultrasound(trig=0, echo=1)  # 定义一个超声波
us.get_distance()  # 获得测量的距离

# 2 获得实时测量的距离
while True:
    print("测量的距离: ", us.get_distance())
    sleep(1)  # 每秒刷新一次
