import RPi.GPIO as GPIO

from src.coap.coapServer import setup_coap_server, add_led_resource, start_coap_server
from src.models.LED import LED

LED_PIN_RED = 23

def gpio_setup():
    GPIO.setwarnings(False)                 # Ignore warning for now
    GPIO.setmode(GPIO.BCM)                  # use the GPIO numbers instead of the “standard” pin numbers


def setup():
    gpio_setup()


def main():
    print("Start main...")
    setup()
    led_red = LED(LED_PIN_RED)
    led_red.test()
    print("Startup complete...")
    setup_coap_server()
    add_led_resource(led_red)
    start_coap_server()


if __name__ == '__main__':
    main()
