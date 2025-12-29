from collections import defaultdict


rules = defaultdict(set)
rules2 = defaultdict(set)
updates = []
try:
    while s := input():
        X,Y = s.split('|')
        rules[int(Y)].add(int(X))
        rules2[int(X)].add(int(Y))
    while s := input():
        updates.append([int(a) for a in s.split(',')])
except:
    pass

def isValid(update):

    for i in range(len(update)-1,-1,-1):
        page = update[i]
        if page not in rules:
            continue
        reqs = update[i+1:]
        for req in reqs:
            if req in rules[page]:
                return False
    return True

sum = 0
for update in updates:
    L = len(update)
    if not isValid(update):
        i = 0
        while i < L:
            io = i
            for j in range(i+1, L):
                if update[j] in rules[update[i]]:
                    update[i], update[j] = update[j], update[i]
                    i = j
            if i == io:
                i += 1
            else:
                i = io
        update_sorted = sorted(update, key = lambda x: len(rules[x]))
        sum += update_sorted[len(update_sorted)//2]

print(sum)