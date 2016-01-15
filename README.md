# gif\_to\_sprite python script

### Usage

`python gif_to_sprite.py example/derp-horse.gif example/master.jpg`

### Basics

There's one command line flag for 'messy' - ie, don't delete intermediary
frames that are extracted from the gif.

`python gif_to_sprite.py -m example/derp-horse.gif example/master.jpg`

This will result in {0, 1, 2, ...}.gif being placed in current working dir.
These files correspond to frames extracted from the gif, in order.
