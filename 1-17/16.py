from PIL import Image
import numpy as np
import sys

im = Image.open('mozart.gif')
a = np.array(im)
print a.shape
# print a
L = list(im.getdata())
pL = list()

for i in range(0, len(L), 640):
    sL = L[i:i+640]
    i = sL.index(195)
    sL = sL[i:] + sL[:i]
    pL.append(sL)

a = np.array(pL, dtype='uint8')
a.shape = (480,640)
im2 = Image.fromarray(a)
im2.save('16.png')
