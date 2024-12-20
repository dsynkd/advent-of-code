from collections import Counter


L,R = list(), list()
while True:
    try:
        s = input().split('   ')
        a,b = int(s[0]), int(s[1])
        L.append(a)
        R.append(b)
    except EOFError:
        break

counter = Counter(R)
similarity_score = 0
for n in L:
    similarity_score += n * counter[n]

print(similarity_score)