#  Tomogo_helper.py
import RPi.GPIO as GPIO

def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)  