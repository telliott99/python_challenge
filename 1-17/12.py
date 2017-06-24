fn = 'evil2.gfx'
fh = open(fn, 'rb')
data = fh.read()

store = [[],[],[],[],[]]
sfxL = ['jpg','png','gif','png','jpg']

for i,c in enumerate(data):
    t = store[i % 5]
    t.append(c)
    
for i,L in enumerate(store):
    fn = '12-' + str(i+1) + '.' + sfxL[i]
    fh = open(fn, 'wb')
    fh.write(''.join(L))
    fh.close()
    
print ''.join(store[3])


