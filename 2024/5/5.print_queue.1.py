from collections import defaultdict


rules = defaultdict(set)
updates = []
try:
    while s := input():
        X,Y = s.split('|')
        # Y needs to be the key because we must check for X's presence when we *encounter Y*
        rules[int(Y)].add(int(X))
    while s := input():
        updates.append([int(a) for a in s.split(',')])
except:
    pass

def isValid(update):

    for i in range(len(update)):
        head = update[i]
        if head not in rules:
            continue
        rest = update[i+1:]
        for page in rest:
            # The pages inside rules must come before not after
            if page in rules[head]:
                return False
    return True

sum = 0
for update in updates:
    if isValid(update):
        sum += update[len(update)//2]

print(sum)