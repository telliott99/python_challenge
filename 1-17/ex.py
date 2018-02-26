import urllib

url = [None, 'http://www.pythonchallenge.com/pc/',
             'http://www.pythonchallenge.com/pc/' ]

def get_challenge(s,i=1):
   return urllib.urlopen(url[i] + s).read()

#print get_challenge('def/ocr.html')
#print get_challenge('def/linkedlist.php?')
#print get_challenge('def/linkedlist.php?nothing=12345')

s = get_challenge('def/oxygen.png')

# a useful library
import StringIO

t = StringIO.StringIO(s)
print dir(t)