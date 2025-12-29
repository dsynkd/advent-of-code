from collections import defaultdict

grid = []
try:
    while line := input():
        grid.append([int(a) if a != '.' else -1 for a in line])
except EOFError:
    pass

m = len(grid)
n = len(grid[0])

visited = set()
t = ()
scores = dict()

def dfs(i,j,prev):
    if not (0 <= i < m) or not (0 <= j < n):
        return
    if grid[i][j] != prev + 1:
        return
    if (i,j) in visited:
        return
    visited.add((i,j))
    if grid[i][j] == 9:
        scores[t] += 1
    prev = grid[i][j]
    dfs(i+1,j,prev)
    dfs(i-1,j,prev)
    dfs(i,j+1,prev)
    dfs(i,j-1,prev)

for i in range(m):
    for j in range(n):
        if grid[i][j] == 0:
            visited = set()
            t = (i,j)
            scores[t] = 0
            dfs(i,j,-1)

sum = 0
for s in scores:
    sum += scores[s]

print(sum)