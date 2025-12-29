grid = []
for line in open(0):
    grid.append(list(line))

M = len(grid)
N = len(grid[0])

visited = set()
region = set()

# Current Plant
p = ''

def isValid(i,j):
    if not (0 <= i < M) or not (0 <= j < N):
        return False
    return grid[i][j] == p

def countNeighbors(i,j):
    c = 0
    d = [(-1,0), (0,-1), (1,0), (0,1)]
    for dx,dy in d:
        if isValid(i+dx, j+dy):
            c += 1
    return c

def countCorners(i,j):
    c = 0
    d = [(-1,1), (1,-1), (1,1), (-1,-1)]
    for dx,dy in d:
        if not (0 <= i+dx < M) or not (0 <= j+dy < N):
            continue
        if grid[i+dx][j] == p and grid[i][j+dy] == p and grid[i+dx][j+dy] != p:
            c += 1
    return c

def dfs(i: int, j: int) -> int:
    if not (0 <= i < M) or not (0 <= j < N):
        return 0
    if (i,j) in region:
        return 0
    if grid[i][j] != p:
        return 0
    visited.add((i,j))
    region.add((i,j))
    
    # count neighbors
    c = countNeighbors(i,j)
    C = 0
    if c == 0:
        return 4
    elif c == 1:
        C = 2
    elif c == 2:
        C = 1
        # Horizontal / Vertical piece
        if isValid(i-1,j) and isValid(i+1,j) or isValid(i,j+1) and isValid(i,j-1):
            C = 0
        else:
            C = 1 + countCorners(i,j)    
    else:
        C = countCorners(i,j)
    return C + dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) + dfs(i,j-1,)

price = 0
for i in range(M):
    for j in range(N):
        p = grid[i][j]
        if (i,j) in visited:
            continue
        region = set()
        sides = dfs(i,j)
        area = len(region)
        cost = sides * area
        price += cost

print(price)