# may not work if user-agent or header reqd

import sys, urllib2
url = sys.argv[1]

def load(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    page = response.read()
    response.close()
    return page

page = load(url)
print page
