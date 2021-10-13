from time import time, sleep
import GPIO


class Ultrasound:
    trig = int()
    echo = int()
    distance = float()

    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        # 信号发送端 设置为输出
        GPIO.setup(self.trig, GPIO.OUT, initial=GPIO.LOW)
        # 信号接收端 设置为输入
        GPIO.setup(self.echo, GPIO.IN)

    def get_distance(self):
        '''
        获得障碍物到传感器的距离。
        主要分为三步：发射信号 接收信号 计算距离。
        '''
        # 第一步 发射测距信号
        GPIO.output(self.trig, GPIO.LOW)
        sleep(2 / 1000000)  # 延时2us
        GPIO.output(self.trig, GPIO.HIGH)
        sleep(10 / 1000000)  # 延时10us
        GPIO.output(self.trig, GPIO.LOW)

        # 第二步 接收脉冲信号
        start_time = None  # 记录低电平结束时间
        end_time = None  # 记录高电平结束时间

        while GPIO.input(self.echo) == GPIO.LOW:
            start_time = time()
        while GPIO.input(self.echo) == GPIO.HIGH:
            end_time = time()
        pulse_time = end_time - start_time  # 脉冲时间

        # 第三步 计算测量距离
        # 公式：(pulse_time * 34300(声速34300cm/s)) / 2 (往返) (单位：cm)
        self.distance = (pulse_time * 34300) / 2

        # 函数返回值为测量的距离
        return self.distance

    def __del__(self):
        GPIO.clearup()
