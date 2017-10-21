#! /usr/bin/python

# split-gif
# Jordan Timmerman

import sys
import os
from PIL import Image

def split (gif):
    gif = sys.argv[1]

    print('%s will be split...' % gif)

    frame = Image.open(gif)
    frameIdx = 0

    try:
        while 1:
            print('\tseek frame %d' % frameIdx)
            frame.seek( frameIdx )
            print('\tsave frame %d' % frameIdx)
            frame.save( '%s/%s.gif' % (os.getcwd(), frameIdx), 'GIF' )
            frameIdx += 1
    except EOFError:
        print('done.')
        pass

if __name__ == '__main__':
    split(sys.argv[1])
