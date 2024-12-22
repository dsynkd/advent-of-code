from collections import defaultdict

state = defaultdict(int)
for a in input().split(','):
    state[int(a)] += 1

N = 256

while N > 0:
    e = [(k,state[k]) for k in state]
    for k,v in e:
        if k == 0:
            state[6] += v
            state[8] += v
        else:
            state[k-1] += v
        state[k] -= v
        if not state[k]:
            del state[k]
    N -= 1

sum = 0
for k in state:
    sum += state[k]
print(sum)