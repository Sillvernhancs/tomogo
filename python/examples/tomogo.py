#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
import logging
import time
import traceback
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont
from waveshare_epd import epd2in13_V4

def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button on GPIO 5
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button on GPIO 6

def render_text(epd, text, font):
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, font=font, fill=0)
    epd.displayPartial(epd.getbuffer(image))

def main():
    logging.basicConfig(level=logging.DEBUG)

    picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
    libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

    if os.path.exists(libdir):
        sys.path.append(libdir)

    epd = epd2in13_V4.EPD()
    init_gpio()

    try:
        logging.info("epd2in13_V4 Demo")
        
        epd.init_fast()
        epd.Clear(0xFF)

        font50 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 50)

        while True:
            logging.info("Waiting on Input")
            if GPIO.input(5) == GPIO.LOW:
                logging.info("Button 5 pressed - Rendering YES")
                render_text(epd, "YES", font50)
                time.sleep(1)
            elif GPIO.input(6) == GPIO.LOW:
                logging.info("Button 6 pressed - Rendering NO")
                render_text(epd, "NO", font50)
                time.sleep(1)
    except IOError as e:
        logging.info(e)
    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd2in13_V4.epdconfig.module_exit(cleanup=True)
        exit()

if __name__ == "__main__":
    main()
