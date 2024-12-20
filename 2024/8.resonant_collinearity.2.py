from collections import defaultdict
import sys

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
            M = 0
            while 0 <= (ax := p1[0] - dx * M) < m and 0 <= (ay := p1[1] - dy * M) < n:
                antinodes.add((ax,ay))
                M += 1

print(len(antinodes))