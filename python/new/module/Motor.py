import GPIO
from time import sleep


class Motor:
    channelA = [20, 21, 16]  # AIN1 AIN2 ENA
    channelB = [19, 26, 13]  # BIN1 BIN2 ENB

    PWMA = None
    PWMB = None

    def __init__(self, channelA, channelB):
        self.channelA = channelA
        self.channelB = channelB

        GPIO.setup(self.channelA[0], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.channelA[1], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.channelA[2], GPIO.OUT, initial=GPIO.HIGH)

        GPIO.setup(self.channelB[0], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.channelB[1], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.channelB[2], GPIO.OUT, initial=GPIO.HIGH)

        self.PWMA = GPIO.PWM(self.channelA[2], 2000)
        self.PWMB = GPIO.PWM(self.channelB[2], 2000)

        self.PWMA.start(0)
        self.PWMB.start(0)

    # 前进后退

    def forward(self, dtime=0, speed=50):
        '''
        小车前进。
        dtime: 前进的时间。单位：秒。默认值：0。
        duty: 占空比，反映速度快慢，默认值：50。
        '''
        # 设置电机为正转
        GPIO.output(self.channelA[0], GPIO.HIGH)
        GPIO.output(self.channelA[1], GPIO.LOW)
        GPIO.output(self.channelB[0], GPIO.HIGH)
        GPIO.output(self.channelB[1], GPIO.LOW)
        # 设置占空比 0~100 占空比越大速度越快
        self.PWMA.ChangeDutyCycle(speed)
        self.PWMB.ChangeDutyCycle(speed)
        sleep(dtime)

    def backward(self, dtime=0, speed=50):
        '''
        小车后退。
        dtime: 后退的时间。单位：秒。默认值：0。
        duty: 占空比，反映速度快慢，默认值：50。
        '''
        # 设置电机为正转
        GPIO.output(self.channelA[0], GPIO.LOW)
        GPIO.output(self.channelA[1], GPIO.HIGH)
        GPIO.output(self.channelB[0], GPIO.LOW)
        GPIO.output(self.channelB[1], GPIO.HIGH)
        # 设置占空比 0~100 占空比越大速度越快
        self.PWMA.ChangeDutyCycle(speed)
        self.PWMB.ChangeDutyCycle(speed)
        sleep(dtime)

    # 转向
    def turn_left(self, dtime=0, speed=50):
        '''
        小车左转。
        dtime: 左转的时间。单位：秒。默认值：0。
        duty: 占空比，反映速度快慢，默认值：50。
        '''
        # 设置电机为正转
        GPIO.output(self.channelA[0], GPIO.LOW)
        GPIO.output(self.channelA[1], GPIO.LOW)
        GPIO.output(self.channelB[0], GPIO.HIGH)
        GPIO.output(self.channelB[1], GPIO.LOW)
        # 设置占空比 0~100 占空比越大速度越快
        self.PWMA.ChangeDutyCycle(0)
        self.PWMB.ChangeDutyCycle(speed)
        sleep(dtime)

    def turn_right(self, dtime=0, speed=50):
        '''
        小车右转。
        dtime: 右转的时间。单位：秒。默认值：0。
        duty: 占空比，反映速度快慢，默认值：50。
        '''
        # 设置电机为正转
        GPIO.output(self.channelA[0], GPIO.HIGH)
        GPIO.output(self.channelA[1], GPIO.LOW)
        GPIO.output(self.channelB[0], GPIO.LOW)
        GPIO.output(self.channelB[1], GPIO.LOW)
        # 设置占空比 0~100 占空比越大速度越快
        self.PWMA.ChangeDutyCycle(speed)
        self.PWMB.ChangeDutyCycle(0)
        sleep(dtime)

    # 旋转
    def spin_left(self, dtime=0, speed=50):
        '''
        小车左旋转。
        '''
        # 设置电机为正转
        GPIO.output(self.channelA[0], GPIO.LOW)
        GPIO.output(self.channelA[1], GPIO.HIGH)
        GPIO.output(self.channelB[0], GPIO.HIGH)
        GPIO.output(self.channelB[1], GPIO.LOW)
        # 设置占空比 0~100 占空比越大速度越快
        self.PWMA.ChangeDutyCycle(speed)
        self.PWMB.ChangeDutyCycle(speed)
        sleep(dtime)

    def spin_right(self, dtime=0, speed=50):
        '''
        小车右旋转。
        '''
        # 设置电机为正转
        GPIO.output(self.channelA[0], GPIO.HIGH)
        GPIO.output(self.channelA[1], GPIO.LOW)
        GPIO.output(self.channelB[0], GPIO.LOW)
        GPIO.output(self.channelB[1], GPIO.HIGH)
        # 设置占空比 0~100 占空比越大速度越快
        self.PWMA.ChangeDutyCycle(speed)
        self.PWMB.ChangeDutyCycle(speed)
        sleep(dtime)

    # 停止
    def stop(self):
        self.PWMA.ChangeDutyCycle(0)
        self.PWMB.ChangeDutyCycle(0)

    def __def__(self):
        self.PWMA.stop()
        self.PWMB.stop()
        GPIO.cleanup()
