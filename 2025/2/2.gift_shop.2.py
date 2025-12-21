ranges = input().split(',')
res = 0

for r in ranges:
    [i,j] = [int(a) for a in r.split('-')]
    for a in range(i,j+1):
        # Sliding window
        s = str(a)
        for l in range(1,len(s)//2+1):
            found = True
            for i in range(0,len(s)-l,l):
                j = i+l
                if s[i:j] != s[j:j+l]:
                    found = False
                    break
            if found:
                res += a
                break

print(res)