grid = []
try:
    while s := input():
        grid.append(list(s))
except:
    pass

m = len(grid)
n = len(grid[0])

blocks = set()
direction = [(-1,0), (0,1), (1,0), (0,-1)]

def find_guard_pos() -> tuple[int,int]:
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '^':
                return (i,j)
    return 0,0

(I,J) = find_guard_pos()

def has_cycle(grid,I,J) -> bool:
    di = 0
    i,j = I,J
    while 0 <= i < m and 0 <= j < n:
        d = direction[di]
        if grid[i][j] == '#':
            if (di,i,j) in blocks:
                return True
            blocks.add((di,i,j))
            i -= d[0]
            j -= d[1]
            di = (di + 1) % len(direction)
        else:
            i += d[0]
            j += d[1]
    return False

count = 0
for i in range(m):
    for j in range(n):
        blocks = set()
        if grid[i][j] == '^' or grid[i][j] == '#':
            continue
        grid[i][j] = '#'
        if has_cycle(grid,I,J):
            count += 1
        # backtrack
        grid[i][j] = '.'

print(count)