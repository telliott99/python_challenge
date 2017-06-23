# http://www.pythonchallenge.com/pc/def/linkedlist.html
# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib2

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

def get(s):
    url2 = url + '?nothing=' + s
    req = urllib2.Request(url2)
    response = urllib2.urlopen(req)
    page = response.read()
    response.close() # its always safe to close an open connection
    last = page.strip().split()
    return last[-1]

n = '12345'
counter = 0
while True:
    counter += 1
    print counter, n
    if counter > 400:
        break
    n = get(n)

# 358 peak.html

# http://www.pythonchallenge.com/pc/def/peak.html