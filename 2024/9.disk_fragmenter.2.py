from collections import defaultdict


disk_map = input()

block_map = []
id = 0
free_space = dict()
file_len = defaultdict(int)
for i in range(len(disk_map)):
    d = int(disk_map[i])
    if i % 2 == 1:
        l = len(block_map)
        block_map += [-1] * d
        free_space[id-1] = [l,d]
    else:
        block_map += [id] * d
        file_len[id] = d
        id += 1

# print(''.join(['.' if a == -1 else str(a) for a in block_map]))

j = len(block_map)-1
jid = id-1
while jid >= 0:
    if block_map[j] != jid:
        j -= 1
        continue
    
    for f in free_space:
        fs = free_space[f]
        if fs[1] >= file_len[jid]:
            for z in range(file_len[jid]):
                block_map[fs[0]], block_map[j] = block_map[j], block_map[fs[0]]
                j -= 1
                fs[1] -= 1
                fs[0] += 1
            break

    jid -= 1

checksum = 0
for i in range(len(block_map)):
    if block_map[i] == -1:
        continue
    checksum += i * block_map[i]

print(checksum)