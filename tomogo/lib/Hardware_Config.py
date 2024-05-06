#  Tomogo_helper.py
import RPi.GPIO as GPIO

def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
    GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
    GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
    GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)  