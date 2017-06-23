from PIL import Image
import numpy as np

im = Image.open('cave.jpg')
L = list(im.getdata())
a = np.array(im)
# print len(L)   # 307200 = 640 wd * 480 ht, triplets

b = list()

for i,row in enumerate(a):
    if i % 2 == 1:
        sL = [row[j] for j in range(1,len(row),2)]
    else:
        sL = [row[j] for j in range(0,len(row),2)]
    sub = np.array(sL)
    b.append(sub)

b = np.array(b, dtype='uint8')
# print b.shape
#(480, 320, 3)

im2 = Image.fromarray(b)
im2.save('new.jpg')
