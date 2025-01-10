#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
import logging
import time
import traceback
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont

# Get the parent directory of the current directory (engine)
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# Append the parent directory to sys.path
sys.path.append(parentdir)

# Define the paths
libdir = os.path.join(parentdir, 'lib')
monstersdir = os.path.join(parentdir, 'monsters')

# import the e ink display 
# from waveshare_epd import epd2in13_V4
from lib.Hardware_Config import init_gpio
from lib.ui.Eink_Display import *

# def render_text(epd, text, font):
#     image = Image.new('1', (epd.height, epd.width), 255)
#     draw = ImageDraw.Draw(image)
#     draw.text((10, 10), text, font=font, fill=0)
#     epd.displayPartial(epd.getbuffer(image))

# def render_tamagotchi(epd, state):
    # image = Image.open(os.path.join(picdir, f'tamagotchi_{state}.bmp'))  # Load Tamagotchi state image
    # epd.displayPartial(epd.getbuffer(image))

def main():
    logging.basicConfig(level=logging.DEBUG)

    init_gpio()

    turn_on_display()
    
    try:
        render_text("┗(^o^　)┓三")
        while True:
            # Check button input
            # if GPIO.input(5) == GPIO.LOW:
                # render_tamagotchi(epd, "happy")  # Render happy Tamagotchi state
                # render_text("┗(^o^　)┓三")
                #print("Button 1 Pressed")
                #time.sleep(1)
            #elif GPIO.input(6) == GPIO.LOW:
                # render_tamagotchi(epd, "sad")    # Render sad Tamagotchi state
                # render_text("三 ┏ ( ˘ω˘ )┛")
                #print("Button 2 Pressed")
                #time.sleep(1)
            #elif GPIO.input(13) == GPIO.LOW:
                # render_tamagotchi(epd, "sad")    # Render sad Tamagotchi state
                # render_text("三 ┏ ( ˘ω˘ )┛")
                #print("Button 3 Pressed")
                #time.sleep(1)
            #elif GPIO.input(26) == GPIO.LOW:
                # render_tamagotchi(epd, "sad")    # Render sad Tamagotchi state
                # render_text("三 ┏ ( ˘ω˘ )┛")
                #print("Button 4 Pressed")
            time.sleep(1)
    except IOError as e:
        logging.info(e)
    except KeyboardInterrupt:
        logging.info("ctrl + c:")

        turn_off_display()

        exit()

if __name__ == "__main__":
    main()
