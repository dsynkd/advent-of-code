fresh = []
fd = open(0)

for line in fd:
    line = line.strip()
    if not line:
        break

    fresh.append(list(map(int, line.strip().split('-'))))

res = 0

for line in fd:
    item = int(line.strip())
    for i,j in fresh:
        if i <= item <= j:
            res += 1
            break

print(res)