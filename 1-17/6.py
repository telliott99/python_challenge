# http://www.pythonchallenge.com/pc/def/channel.zip

import zipfile
z = zipfile.ZipFile('channel.zip')
print z.open('readme.txt').read()
L = list()

def follow(fn):
    fn += '.txt'
    L.append(fn)
    fh = z.open(fn)
    result = fh.read()
    return result.strip().split()[-1]

# so the contents of each file contain the next fn
# 907 46145
# 908 comments.
# 46145 has a hint:  "Collect the comments."

def run():
    fn = '90052'
    for i in range(1000):
        fn = follow(fn)
        if fn == 'comments.':
            break
        # print i, fn

run()
print L[-1]

cL = list()
for fn in L:
    info = z.getinfo(fn)
    cL.append(info.comment)
print ''.join(cL)




    