from module import Track
from time import sleep

# 1 定义一个对象
t = Track()
# 2 使用方法
t.state()  # 获取寻线传感器的状态（重点）
t.order()  # 获取判断后的结果（可选）

# 3 实时获取传感器状态
while True:
    print("传感器状态：", t.state())
    sleep(1)  # 每隔一秒刷新一次
