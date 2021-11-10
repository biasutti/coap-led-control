import RPi.GPIO as GPIO
import time

LED_PIN = 23

def gpio_setup():
    GPIO.setwarnings(False)                 # Ignore warning for now
    GPIO.setmode(GPIO.BCM)                  # use the GPIO numbers instead of the “standard” pin numbers
    GPIO.setup(LED_PIN, GPIO.OUT)


def setup():
    gpio_setup()


def test():
    for i in range(5):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)

    GPIO.cleanup()


def main():
    print("Start main...")
    setup()
    test()
    print("Startup complete...")


if __name__ == '__main__':
    main()
