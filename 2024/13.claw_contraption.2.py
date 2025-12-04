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

ax,ay,bx,by,tx,ty = 0,0,0,0,0,0
cache = []
cost = 0

def dfs(x: int, y: int, ac: int, bc: int):
    if (x,y) == (tx,ty):
        return ac*3 + bc
    if x > tx or y > ty:
        return 0
    if ac > 100 or bc > 100:
        return 0
    if cache[x][y] > -1:
        return cache[x][y]
    res = dfs(x+ax,y+ay,ac+1,bc) or dfs(x+bx,y+by,ac,bc+1)
    cache[x][y] = res
    return res

prize = 0
for m in machines:
    ax,ay = m[0]
    bx,by = m[1]
    tx,ty = m[2]
    cache = [[0 for _ in range(ty+1)] for _ in range(tx+1)]
    for i in range()
    prize += dfs(0,0,0,0)

print(prize)