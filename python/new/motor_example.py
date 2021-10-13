from module import Motor
from time import sleep

# 1 定义一个对象
motor = Motor()         # 创建一个电机


# 2 控制电机
motor.forward(1)        # 前进
motor.backward(1)       # 后退

motor.turn_left(1)      # 左转
motor.turn_right(1)     # 右转

motor.spin_left(1)      # 左旋
motor.spin_right(1)     # 右旋

motor.stop()            # 停止
