lines = []
M = 0

try:
    while s := input():
        s1 = s.split(' -> ')
        x1,y1 = [int(a) for a in s1[0].split(',')]
        x2,y2 = [int(a) for a in s1[1].split(',')]
        lines.append(((x1,y1), (x2,y2)))
        M = max(M,x1,x2,y1,y2)
except:
    pass

M += 1

grid = [[0 for _ in range(M)] for _ in range(M)]
for ((x1,y1), (x2,y2)) in lines:
    if x1 == x2:
        if y1 <= y2:
            for y in range(y1, y2+1):
                grid[y][x1] += 1
        else:
            for y in range(y2, y1+1):
                grid[y][x1] += 1
    elif y1 == y2:
        if x1 <= x2:
            for x in range(x1, x2+1):
                grid[y1][x] += 1
        else:
            for x in range(x2, x1+1):
                grid[y1][x] += 1


sum = 0
for i in range(M):
    for j in range(M):
        if grid[i][j] > 1:
            sum += 1

print(sum)