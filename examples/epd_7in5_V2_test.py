
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in5_V2 Demo")
    epd = epd7in5_V2.EPD()
    
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    font28 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 28)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

    Display = Image.new('1', (epd.width, epd.height), 255)
    unalogo = Image.open(os.path.join(picdir, 'unalogo.bmp'))


    # Drawing on the Vertical image
    logging.info("Drawing on the Vertical image...")
    Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Limage)
    Display.paste(unalogo, (340, 0))
    draw.text((2, 70), 'CS 155 Computer Science I', font = font28, fill = 0)
    draw.text((2, 100), 'Professor: Steven Puckett ', font = font18, fill = 0)
    draw.text((2, 120), 'Email: spuckett1@una.edu Number: 256-765-4312 ', font = font18, fill = 0)
    draw.text((2, 140), 'Class duration: 10:00 AM - 1:00 PM', font = font18, fill = 0)
    draw.line((0, 180, 800, 180), fill = 0)
    epd.display(epd.getbuffer(Limage))

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5_V2.epdconfig.module_exit()
    exit()
