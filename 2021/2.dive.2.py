cmds = []
try:
    while s := input():
        s = s.split(' ')
        cmds.append((s[0], int(s[1])))
except EOFError:
    pass

position,depth,aim = 0,0,0

for cmd,v in cmds:
    if cmd == "forward":
        position += v
        depth += aim * v
    elif cmd == "down":
        aim += v
    elif cmd == "up":
        aim -= v

print(depth * position)