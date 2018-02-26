# source from
# http://www.pythonchallenge.com/pc/def/equality.html

from utils import load
from string import letters as lt

data = load('3.txt')
for c in data:
    if not c in lt and c != '\n':
        print c

import re
s = '[a-z]'
S = '[A-Z]'
sL = [s,S,S,S,s,S,S,S,s]
p = re.compile(''.join(sL))
L = p.findall(data)
print ''.join(L)

'''
> python 3b.py
['qIQNlQSLi', 'eOEKiVEYj', 'aZADnMCZq', 'bZUTkLYNg', 'uCNDeHSBj', 'kOIXdKBFh', 'dXJVlGZVm', 'gZAGiLQZx', 'vCJAsACFl', 'qKWGtIDCj']
>
'''

# http://www.pythonchallenge.com/pc/def/linkedlist.html

# returns linkedlist.php

# http://www.pythonchallenge.com/pc/def/linkedlist.php

