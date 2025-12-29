grid = []
for line in open(0):
    grid.append(line.split())

n = len(grid)
m = len(grid[0])

total = 0

for j in range(m):
    op = grid[-1][j]
    res = 0 if op == '+' else 1
    for i in range(n-2,-1,-1):
        if op == '+':
            res += int(grid[i][j])
        else:
            res *= int(grid[i][j])
    total += res

print(total)