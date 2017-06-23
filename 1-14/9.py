import matplotlib.pyplot as plt

fn = 'data/9.txt'
fh = open(fn)
data = fh.read()
fh.close()

blocks = data.strip().split('\n\n')

def get_ints(s):
    values = s.strip().split(':')[1].strip()
    L = values.split(',')
    return [int(s) for s in L]

first = get_ints(blocks[1])
second = get_ints(blocks[2])

for i in range(0,len(first),2):
    x,y = first[i:i+2]
    plt.scatter(x,y,c ='k')

for i in range(0,len(second),2):
    x,y = second[i:i+2]
    plt.scatter(x,y,c ='r')

plt.savefig('figs/saved.png')
