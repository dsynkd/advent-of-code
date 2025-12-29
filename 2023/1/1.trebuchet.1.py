res = 0

for line in open(0):
    line = line.strip()
    val = ''
    for i in range(len(line)):
        if line[i].isdigit():
            val += line[i]
            break
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            val += line[i]
            break
    res += int(val)

print(res)