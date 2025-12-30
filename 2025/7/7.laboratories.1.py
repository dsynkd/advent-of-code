grid = []
for line in open(0):
    grid.append(list(line.strip()))

n = len(grid)
m = len(grid[0])

visited = set()

def dfs(i,j):
    if not (0 <= i < n and 0 <= j < m):
        return
    if((i,j) in visited):
        return
    
    if grid[i][j] == '^':
        dfs(i, j+1)
        dfs(i, j-1)
        return
    visited.add((i,j))
    return dfs(i+1, j)

for j in range(m):
    if grid[0][j] == 'S':
        dfs(0,j)
        break

res = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '^' and (i-1,j) in visited:
            res += 1

print(res)