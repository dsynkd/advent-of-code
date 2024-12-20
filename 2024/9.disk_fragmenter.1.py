disk_map = input()

block_map = []
id = 0
for i in range(len(disk_map)):
    d = int(disk_map[i])
    if i % 2 == 1:
        block_map += [-1] * d
    else:
        block_map += [id] * d
        id += 1

j = len(block_map)-1
i = 0
while i < j:
    if block_map[j] == -1:
        j -= 1
        continue
    if block_map[i] != -1:
        i += 1
        continue
    block_map[i], block_map[j] = block_map[j], block_map[i]

checksum = 0
for i in range(len(block_map)):
    if block_map[i] == -1:
        break
    checksum += i * block_map[i]

print(checksum)