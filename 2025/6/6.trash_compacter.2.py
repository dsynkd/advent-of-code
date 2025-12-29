lines = []
for line in open(0):
    # Only take off newline, not trailing whitespace
    lines.append(line[:-1])

# K is list of column lengths
K = []
c = 0
for j in range(1, len(lines[-1])):
    if lines[-1][j] != ' ':
        K.append(c)
        c = 0
    else:
        c += 1
K.append(c+1)

ops = lines[-1].split()

grid = []
for i in range(len(lines)-1):
    j = 0
    row = []
    K_i = 0
    while j < len(lines[i]):
        k = K[K_i]
        row.append(lines[i][j:j+k])
        j += k + 1
        K_i += 1
    grid.append(row)

n = len(grid)
m = len(grid[0])

total = 0

for j in range(m):
    op = ops[j]
    res = 0 if op == '+' else 1
    
    k = K[j]
    
    for c in range(k):
        num = ''
        for i in range(n):
            if grid[i][j][c] != ' ':
                num += grid[i][j][c]
        
        if op == '+':
            res += int(num)
        else:
            res *= int(num)
    
    total += res

print(total)