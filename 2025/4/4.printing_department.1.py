grid = []

for line in open(0):
    grid.append(list(line.strip()))

n = len(grid)
m = len(grid[0])

def neighbor_val(i,j):
    if not (0 <= i < n and 0 <= j < m):
        return 0
    if grid[i][j] == '@':
        return 1
    return 0

def count_neighbors(i,j):
    return (neighbor_val(i+1,j) +
            neighbor_val(i+1,j+1) +
            neighbor_val(i+1,j-1) +
            neighbor_val(i,j+1) +
            neighbor_val(i,j-1) +
            neighbor_val(i-1,j) +
            neighbor_val(i-1,j+1) +
            neighbor_val(i-1,j-1))

res = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '@' and count_neighbors(i,j) < 4:
            res += 1

print(res)