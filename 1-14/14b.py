from PIL import Image
import numpy as np

im = Image.open('wire.png')
print im.size
im2 = im.resize((100,100))
print im2.size
im2.save('wire2.png')