#  Tomogo_helper.py
import RPi.GPIO as GPIO

def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button on GPIO 5
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button on GPIO 6
