import numpy as np
from math import modf

machines = []
try:
    while True:
        a = input().split(':')[1]
        b = input().split(':')[1]
        c = input().split(':')[1]
        a =[x.strip() for x in a.split(', ')]
        a = [int(x.split('+')[1]) for x in a]
        b =[x.strip() for x in b.split(', ')]
        b = [int(x.split('+')[1]) for x in b]
        c =[x.strip() for x in c.split(', ')]
        c = [int(x.split('=')[1]) for x in c]
        machines.append([
            (a[0],a[1]),
            (b[0],b[1]),
            (c[0],c[1])
        ])
        z = input()
        if z == '-':
            raise EOFError
except EOFError:
    pass

res = 0

for m in machines:
    ax,ay = m[0]
    bx,by = m[1]
    tx,ty = m[2]
    tx += 10000000000000
    ty += 10000000000000
    
    A = np.array([[ax, bx],
                  [ay, by]])
    A1 = np.array([[tx, bx],
                    [ty, by]])
    A2 = np.array([[ax, tx],
                    [ay, ty]])
    
    x = np.linalg.det(A1) / np.linalg.det(A)
    y = np.linalg.det(A2) / np.linalg.det(A)
    xf, _ = modf(x)
    yf, _ = modf(y)
    
    f1 = round(xf * 100)
    f2 = round(yf * 100)
    
    if((f1 == 0 or f1 == 100) and (f2 == 0 or f2 == 100)): # We have solution!
        res += round(x) * 3 + round(y)

print(res)