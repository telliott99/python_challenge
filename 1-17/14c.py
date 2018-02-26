'''
10 x 10

round 0:  the outer circle is

  0  1  2  3  4  5  6  7  8  9  
 10                         19
 20                         29
 30                         39
 40                         49
 50                         59
 60                         69
 70                         79
 80                         89
 90 91 92 93 94 95 96 97 98 99                                                                                                                                            

round 1 starts with 11

'''

SZ = 100
n = SZ
L = list()
n = 100
v = True

while n > 2:
    if v:
        print 'n', str(n).rjust(3)
    o = (SZ-n)/2
    i = SZ*o + o
    
    top = range(i,i+n)
    #print 'top',  top[0], top[-1]
    L.append(top)
    
    # a range, so not steps-1
    n -= 1
    i = L[-1][-1] + SZ
    right = range(i, SZ*SZ, SZ)[:n]
    #print 'right', right[0], right[-1]
    L.append(right)
    
    #n -= 1
    i = L[-1][-1] - 1
    bottom = range(i, i-n, -1)
    #print 'bottom', bottom[0], bottom[-1]
    L.append(bottom)
    
    i = L[-1][-1]
    left = range(i - SZ, top[0], -SZ)
    L.append(left)
    n -= 1
    
    if v:
        for sL in L[-4:]:
            print str(sL[0]).rjust(5),
            print str(sL[-1]).rjust(5)


L.extend([[4949,4950],[5050],[5049]])
pL = list()
for sL in L:
    pL.extend(sL)
    
print len(pL)
print sorted(pL) == range(10000)

'''
n 100
    0    99
  199  9999
 9998  9900
 9800   100
n  98
  101   198
  298  9898
 9897  9801
 9701   201
n  96
  202   297
  397  9797
 9796  9702
 9602   302
...
10000
True
'''

from PIL import Image
import numpy as np

im = Image.open('wire.png')
iL = list(im.getdata())

iL2 = [False] * 10000
for i,v in enumerate(iL):
    j = pL[i]
    iL2[j] = v

a = np.array(iL2, dtype='uint8')
a.shape = (100,100,3)

im2 = Image.fromarray(a)
im2.save('14c.png')


