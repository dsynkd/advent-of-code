dial = 50
res = 0

while True:
    try:
        line = input()
        val = int(line[1:])
        if line[0] == 'L':
            res += (100 - dial + val) // 100
            if dial == 0:
                res -= 1
            dial = (dial - val) % 100
        elif line[0] == 'R':
            res += (dial + val) // 100
            dial = (dial + val) % 100
    except EOFError:
        break

print(res)