from collections import defaultdict

grid = []
try:
    while line := input():
        grid.append(list(line))
except EOFError:
    pass


m = len(grid)
n = len(grid[0])
antennas = defaultdict(list)
for i in range(m):
    for j in range(n):
        if grid[i][j] != '.':
            antennas[grid[i][j]].append((i,j))

count = 0
antinodes = set()
for a in antennas:
    p = antennas[a]
    for p1 in p:
        for p2 in p:
            if p1 == p2:
                continue
            dx,dy = (p2[0] - p1[0]), p2[1] - p1[1]
            ax,ay = p1[0] - dx, p1[1] - dy
            if 0 <= ax < m and 0 <= ay < n:
                antinodes.add((ax,ay))

print(len(antinodes))