
import sys
import os
import logging
import time
import traceback
from PIL import Image, ImageDraw, ImageFont
from waveshare_epd import epd2in13_V4

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')

epd = epd2in13_V4.EPD()
TextFont = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 40)

def render_text(text, font = picdir):
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, font=font, fill=0)
    epd.displayPartial(epd.getbuffer(image))

def turn_off_display():
    epd.Clear(0xFF)
    epd.sleep()
    epd2in13_V4.epdconfig.module_exit(cleanup=True)

def turn_on_display():
    epd.init_fast()
    epd.Clear(0xFF)