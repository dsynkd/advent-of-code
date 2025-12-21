dial = 50
res = 0

while True:
    try:
        line = input()
        val = int(line[1:])
        div, mod = divmod(val, 100)
        res += div

        if line[0] == 'L':
            if dial != 0 and dial - mod <= 0:
                res += 1
            dial = (dial - val) % 100
        elif line[0] == 'R':
            if dial + mod >= 100:
                res += 1
            dial = (dial + val) % 100

    except EOFError:
        break

print(res)