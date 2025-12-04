# It works within a reasonable time but is still slow in my opinion

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

prize = 0
for m in machines:
    ax,ay = m[0]
    bx,by = m[1]
    tx,ty = m[2]
    cost = float('inf')
    for i in range(100):
        for j in range(100):
            x = ax*i + bx*j
            y = ay*i + by*j
            if (x,y) == (tx,ty):
                cost = min(cost, i*3+j)
    if cost != float('inf'):
        prize += cost

print(prize)