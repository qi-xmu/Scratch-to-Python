# ! /usr/bin/python
# 这是一个led模块
# 需要实现的功能： 点灯 闪烁 按键控制

import GPIO


class LED:
    channel = 0
    pwm = None

    def __init__(self, channel, Hz=2000):

        # 构造函数
        self.channel = channel
        GPIO.setup(channel, GPIO.OUTPUT)
        self.pwm = GPIO.pwm(self.channel, Hz)
        self.pwm.start(0)

    def turn_on(self):
        # 点亮
        self.pwm.ChangeDutyCycle(100)

    def turn_off(self):
        # 熄灭
        self.pwm.ChangeDutyCycle(0)

    def brightness(self, duty=50):
        # 设置亮度
        self.pwm.ChangeDutyCycle(duty)

    def state(self):
        # 状态
        return GPIO.input(self.channel)

    def __del__(self):
        self.pwm.stop()
        GPIO.clearup()


class Button:
    channel = 0
    led = LED()

    def __init__(self, channel):
        self.channel = channel
        GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def press(self):
        # 按下
        state = self.led.zhuang_tai()  # ???? 需要测试
        if state == GPIO.LOW:
            self.led.dian_liang()
        else:
            self.led.xi_mie()

    def bind(self, led):
        # 绑定
        self.led = led
        GPIO.add_event_detect(self.channel, GPIO.RISING,
                              callback=self.press, bouncetime=200)
