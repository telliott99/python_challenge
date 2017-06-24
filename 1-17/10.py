def get_reps(s):
    L = [[1,s[0]]]
    for c in s[1:]:
        if c == L[-1][1]:
            L[-1][0] += 1
        else:
            L.append([1,c])            
    rL = list()
    for e in L:
        rL.append(str(e[0]))
        rL.append(e[1])
    return ''.join(rL)

curr = '1'
L = [curr]
for i in range(30):
    next = get_reps(curr)   
    curr = next
    L.append(curr)
    
print L[:5]
print len(L[30])