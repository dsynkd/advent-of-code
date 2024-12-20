cmds = []
try:
    while s := input():
        s = s.split(' ')
        cmds.append((s[0], int(s[1])))
except EOFError:
    pass

position = 0
depth = 0
for cmd,v in cmds:

    if cmd == "forward":
        position += v
    elif cmd == "down":
        depth += v
    elif cmd == "up":
        depth -= v

print(depth * position)