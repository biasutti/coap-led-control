import sys
import signal

import RPi.GPIO as GPIO

from coap.coapServer import setup_coap_server, add_led_resource, start_coap_server
from models.LED import LED

LED_PIN_RED = 23

sensors = []

def gpio_setup():
    GPIO.setwarnings(False)                 # Ignore warning for now
    GPIO.setmode(GPIO.BCM)                  # use the GPIO numbers instead of the “standard” pin numbers


def setup():
    gpio_setup()


def main():
    global sensors
    print("Start main...")
    setup()
    led_red = LED("led-01", LED_PIN_RED)
    led_red.test()
    sensors.append(led_red)
    print("Startup complete...")
    setup_coap_server()
    add_led_resource(led_red)
    start_coap_server(sensors)


def close():
    GPIO.cleanup()


def signal_handler(sig, frame):
    close()
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
