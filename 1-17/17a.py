import cookielib, urllib2, urllib, re, bz2, time, xmlrpclib
 
start = time.time()
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
 
def get_cookie_info(url):
    request = urllib2.Request(url)
    
    # http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=
    print 'url:', url.split('=')[1]
    # prints a number, like 44827
    
    response = opener.open(request)
    cookies = cj.make_cookies(response, request)
    text = urllib.urlopen(url).read()
    
    print 'response:', text
    '''
    <body>
<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough. -->
    '''
    
    digits = ''.join(re.findall(r'busynothing is (\d+)', text))
    info = urllib.unquote_plus(cookies[0].value)
    return digits, info
 
# this is the url for level 4 (hence the chain in the image)
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

# print get_cookie_info(url)
# ('', 'you should have followed busynothing...')

new_url = url + '?busynothing='
num = '12345'
num, info = get_cookie_info(new_url + num)
print '0'
print
print num, info

# we build up the info coming back into 'out'
# next part takes a while
out = info
counter = 0

while True:
    counter += 1
    print str(counter).rjust(3) 
    num, info = get_cookie_info(new_url + num)
    out += info
    print num, info
    try:
        int(num)
    except:
        break
    #if counter == 5:
        #break

print 'out:', repr(out)
# print bz2.decompress(urllib.unquote_plus(out))

msg = 'BZh91AY&SY\x94:\xe2I\x00\x00!\x19\x80P\x81\x11\x00\xafg\x9e\xa0 \x00hE=M\xb5#\xd0\xd4\xd1\xe2\x8d\x06\xa9\xfa&S\xd4\xd3!\xa1\xeai7h\x9b\x9a+\xbf`"\xc5WX\xe1\xadL\x80\xe8V<\xc6\xa8\xdbH&32\x18\xa8x\x01\x08!\x8dS\x0b\xc8\xaf\x96KO\xca2\xb0\xf1\xbd\x1du\xa0\x86\x05\x92s\xb0\x92\xc4Bc\xf1w$S\x85\t\tC\xae$\x90'

bz2.BZ2Decompressor().decompress(urllib.unquote_plus(''.join(message))
