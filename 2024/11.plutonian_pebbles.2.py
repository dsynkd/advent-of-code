from collections import defaultdict

line = input()
counter = defaultdict(int)
for a in line.split(' '):
    counter[int(a)] += 1

n = 75

while n > 0:
    e = [(k,counter[k]) for k in counter]
    for p,v in e:
        if p == 0:
            counter[1] += v
        else:
            sp = str(p)
            lp = len(str(p))
            if lp % 2 == 0:
                l = lp // 2
                counter[int(sp[:l])] += v
                counter[int(sp[l:])] += v
            else:
                counter[p * 2024] += v
        counter[p] -= v
        if not counter[p]:
            del counter[p]
    n -= 1

sum = 0
for c in counter:
    sum += counter[c]
print(sum)