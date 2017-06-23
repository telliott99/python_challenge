n = 100
count = 0
while n > 0:
    sub = n + 2*(n-1) + n-2
    count += sub
    n -= 2

print count