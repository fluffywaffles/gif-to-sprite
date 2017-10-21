#!/usr/bin/python

# from http://oranlooney.com/make-css-sprites-python-image-library/
# Orignial Author Oran Looney <olooney@gmail.com>

# mods by Josh Gourneau <josh@gourneau.com> to make one big horizontal sprite
# JPG with no spaces between images

# EDIT 1-14-16 by Jordan Timmerman (@skorlir) to work directly with split-gif

import os
from PIL import Image
import glob
import sys
import re

def make_spritesheet (mastername):
    if mastername is None:
        mastername = 'master.jpg'

    iconMap = [ fn for fn in glob.glob('*.gif') if re.match(r'\d+.gif', fn) ]

    # sort per name format: {frame-number}.gif
    iconMap = sorted(iconMap, key=lambda i: int(i.split('.')[0]))

    images = [ Image.open(filename) for filename in iconMap ]

    image_width, image_height = images[0].size

    print ( 'all images assumed to be %d by %d.' % (image_width, image_height) )

    master_width  = image_width * len(images)
    master_height = image_height

    print ( 'the spritesheet will by %d by %d' % (master_width, master_height) )

    print ( 'combining %d frames into spritesheet...' % len(images) )
    master = Image.new(
        mode  = 'RGBA',
        size  = (master_width, master_height),
        color = (0, 0, 0, 0)  # fully transparent
    )

    print ( 'blank spritesheet created' )

    print ( 'filling sprites...' )
    for count, image in enumerate(images):
        location = image_width * count
        print ( '\tplace frame %s at %d px...' % (count, location) )
        master.paste(image, (location, 0))
    print ( 'spritesheet filled' )

    print ( 'saving spritesheet as %s...' % mastername )
    master.save(mastername, transparency=0)
    print ( 'saved!' )

if __name__ == '__main__':
    make_spritesheet(sys.argv[1] if 1 < len(sys.argv) else None)
