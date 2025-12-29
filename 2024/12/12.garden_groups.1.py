grid = []
for line in open(0):
    grid.append(list(line))

M = len(grid)
N = len(grid[0])

visited = set()
region = set()

def dfs(i: int, j: int, p: str) -> int:
    if not (0 <= i < M) or not (0 <= j < N):
        return 1
    if (i,j) in region:
        return 0
    if grid[i][j] != p:
        return 1
    visited.add((i,j))
    region.add((i,j))
    return dfs(i+1,j,p) + dfs(i,j+1,p) + dfs(i-1,j,p) + dfs(i,j-1,p)

price = 0
for i in range(M):
    for j in range(N):
        p = grid[i][j]
        if (i,j) in visited:
            continue
        region = set()
        perimeter = dfs(i,j,p)
        area = len(region)
        cost = perimeter * area
        price += cost

print(price)