# http://www.pythonchallenge.com/pc/def/ocr.html

fn = '2.txt'
fh = open(fn)
data = fh.read()
fh.close()

bad = '!@#$%^&*()[]{}+_- '
L = [c for c in data if not c in bad]
L = [c for c in L if not c == '\n']
print ''.join(L)

'''
> python 2b.py 
equality
> 
'''

# http://www.pythonchallenge.com/pc/def/equality.html