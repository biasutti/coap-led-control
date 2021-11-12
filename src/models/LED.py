import time

from RPi import GPIO

class LED:

    def __init__(self, pin):
        super().__init__()
        self.pin = pin
        self.power_state = False
        GPIO.setup(pin, GPIO.OUT)


    def on(self):
        if not self.power_state:
            GPIO.output(self.pin, GPIO.HIGH)
            self.power_state = True


    def off(self):
        if self.power_state:
            GPIO.output(self.pin, GPIO.LOW)
            self.power_state = False


    def test(self):
        for i in range(3):
            self.on()
            time.sleep(1)
            self.off()
            time.sleep(1)
