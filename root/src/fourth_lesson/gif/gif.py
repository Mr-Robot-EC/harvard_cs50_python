# pillow.readthedocs.io
"""
python gif.py horse_1.gif horse_2.gif
In this way we created the gif horse.gif
"""
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "horse.gif", save_all=True, append_images=images[1:], duration=200, loop=0
)