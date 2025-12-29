grid = []
try:
    while s := input():
        grid.append(s)
except:
    pass

m = len(grid)
n = len(grid[0])

def find_guard_pos() -> tuple[int,int]:
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '^':
                return (i,j)
    return 0,0

blocks = set()
visited = set()
direction = [(-1,0), (0,1), (1,0), (0,-1)]
di = 0
(i,j) = find_guard_pos()

# Need to do iteratively, otherwise get maximum recursion depth exceeded
while 0 <= i < m and 0 <= j < n:
    d = direction[di]
    if grid[i][j] == '#':
        # Check for cycle, even though problem implies that there should not be one
        if (di,i,j) in blocks:
            break
        blocks.add((di,i,j))
        i -= d[0]
        j -= d[1]
        di = (di + 1) % len(direction)
    else:
        visited.add((i,j))
        i += d[0]
        j += d[1]

print(len(visited))