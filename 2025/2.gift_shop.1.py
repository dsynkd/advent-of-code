ranges = input().split(',')
res = 0

for r in ranges:
    [i,j] = [int(a) for a in r.split('-')]
    for a in range(i,j+1):
        s = str(a)
        l = len(s)
        if l % 2 == 1:
            continue
        if s[:l//2] == s[l//2:]:
            res += a

print(res)