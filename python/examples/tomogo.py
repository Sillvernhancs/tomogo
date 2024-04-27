#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V4
import time
from PIL import Image, ImageDraw, ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

import RPi.GPIO as GPIO
# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button on GPIO 5
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button on GPIO 6

epd = epd2in13_V4.EPD()  # Initialize EPD outside the try block

def render_text(text):
    # Create an image
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)
    
    # Set font and draw text
    draw.text((10, 10), text, font=font50, fill=0)
    
    # Display the image
    epd.displayPartial(epd.getbuffer(image))

try:
    logging.info("epd2in13_V4 Demo")
    
    epd.init_fast()
    epd.Clear(0xFF)

    # Drawing on the image
    font50 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 50)
    
    while True:
        logging.info("Waiting on Input")
        if GPIO.input(5) == GPIO.LOW:
            logging.info("Button 5 pressed - Rendering YES")
            render_text("YES")
            time.sleep(1)  # Add a small delay after rendering text
        elif GPIO.input(6) == GPIO.LOW:
            logging.info("Button 6 pressed - Rendering NO")
            render_text("NO")
            time.sleep(1)  # Add a small delay after rendering text
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V4.epdconfig.module_exit(cleanup=True)
    exit()

