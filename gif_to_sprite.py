#! /usr/bin/python

from split_gif import split
from sprite_from_images import make_spritesheet
import argparse
import os
import glob
import re

def gif_to_sprite (gif=None, mastername=None, cleanup=True):
    split(gif)
    make_spritesheet(mastername)

    if cleanup is True:
        print ('cleaning up...')
        leftovers = [ f for f in glob.glob('*.gif') if re.match(r'\d+.gif', f) ]
        for f in leftovers:
            print ('\tremove %s' % f)
            os.remove(f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Make a spritesheet from an animated gif.'
    )
    parser.add_argument('gif', metavar='gif', type=str, nargs=1)
    parser.add_argument('mastername',
                        help='Output spritesheet name (w/ extension)',
                        metavar='', type=str, nargs='?', default=None)
    parser.add_argument('-m', '--no-cleanup', dest='cleanup',
                        help='leave a mess / don\'t clean up frames',
                        action='store_false')

    args = parser.parse_args()

    gif_to_sprite(gif=args.gif, mastername=args.mastername, cleanup=args.cleanup)
