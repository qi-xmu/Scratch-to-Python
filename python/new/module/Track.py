import GPIO


class Track:
    channels = []

    def __init__(self, channels):
        self.channels = channels
        GPIO.setup(self.channels, GPIO.IN, initial=GPIO.LOW)

    def state(self):
        t1 = GPIO.input(self.channels[0])
        t2 = GPIO.input(self.channels[1])
        t3 = GPIO.input(self.channels[2])
        t4 = GPIO.input(self.channels[3])
        return (t1, t2, t3, t4)

    def order(self):
       # 检测到黑线时循迹模块相应的指示灯亮，端口电平为LOW
       # 未检测到黑线时循迹模块相应的指示灯灭，端口电平为HIGH
        status = self.state()

        out = [-2, -1, 0, 1, 2]  # 左转 --> 右转

        if status[:3] == (0, 0, 1):
            return out[1]  # 小左转
        elif status[1:] == (1, 0, 0):
            return out[3]  # 小右转

        elif status[0] == 0:
            return out[0]  # 左转
        elif status[3] == 0:
            return out[4]  # 右转

        elif status[1] == 0 and status[2] == 1:
            # or
            # elif status[1:3] == (0,1)
            return out[1]  # 小小左转
        elif status[1] == 1 and status[2] == 0:
            # or
            # elif status[1:3] == (1,0)
            return out[3]  # 小小右转

        elif status[1] == 0 and status[2] == 0:
            # or
            # elif status[1:3] == (0,0)
            return out[2]  # 前进

    def __def__(self):
        GPIO.cleanup()
