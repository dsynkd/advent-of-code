grid = []
for line in open(0):
    grid.append(list(line.strip()))

n = len(grid)
m = len(grid[0])

res = 0
cache = dict()

def dfs(i,j):
    if not (0 <= i < n and 0 <= j < m):
        return 1
    if (i,j) in cache:
        return cache[(i,j)]

    if grid[i][j] == '^':
        res = dfs(i, j+1) + dfs(i, j-1)
    else:
        res = dfs(i+1, j)
    cache[(i,j)] = res
    return res

for j in range(m):
    if grid[0][j] == 'S':
        res = dfs(0,j)
        break

print(res)