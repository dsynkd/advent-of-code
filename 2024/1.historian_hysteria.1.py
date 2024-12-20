from bisect import insort

L,R = list(), list()
while True:
    try:
        s = input().split('   ')
        l,r = int(s[0]), int(s[1])
        insort(L,l)
        insort(R,r)
    except EOFError:
        break

sum = 0
for x,y in zip(L,R):
    sum += abs(y-x)

print(sum)