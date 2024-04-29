
import sys
import os
import logging
import time
import traceback
from PIL import Image, ImageDraw, ImageFont



# Assuming Eink_Display.py is located in the 'ui' directory
# Get the current directory of Eink_Display.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate two directories up to reach the parent directory of 'lib'
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))

sys.path.append(parent_dir)


# Construct the path to the 'pic' directory
picdir = os.path.join(parent_dir, 'pic')
print (picdir)

from lib.waveshare_epd import epd2in13_V4

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