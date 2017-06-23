from utils import load
from string import maketrans

s1 = load('1.txt')

tr = maketrans('abcdefghijklmnopqrstuvwxyz',
               'cdefghijklmnopqrstuvwxyzab')
              
s2 = s1.translate(tr)
print s2

s3 = 'map'
print s3.translate(tr)

# ocr