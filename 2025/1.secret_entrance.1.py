dial = 50
res = 0

while True:
    try:
        line = input()
        if line[0] == 'L':
            dial = (dial - int(line[1:])) % 100
        elif line[0] == 'R':
            dial = (dial + int(line[1:])) % 100
        if dial == 0:
            res += 1
    except EOFError:
        break

print(res)