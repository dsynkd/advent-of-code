line = input()
pebbles = [int(a) for a in line.split(' ')]
n = 25

while n > 0:
    np = []
    for p in pebbles:
        if p == 0:
            np.append(1)
        else: 
            sp = str(p)
            lp = len(str(p))
            if lp % 2 == 0:
                l = lp // 2
                np += [int(sp[:l]), int(sp[l:])]
            else:
                np.append(p * 2024)
    pebbles = np
    n -= 1

# print(pebbles)
print(len(pebbles))