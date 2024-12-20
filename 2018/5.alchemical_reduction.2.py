p = input()

minL = len(p)

for c in range(ord('a'), ord('z')):
    polymer = p.replace(chr(c), '').replace(chr(c).upper(), '')

    i = 1
    while i < len(polymer):
        c1 = polymer[i-1]
        c2 = polymer[i]
        if abs(ord(c2) - ord(c1)) == 32:
            polymer = polymer[:i-1] + polymer[i+1:]
            i = 1
        else:
            i += 1
    minL = min(minL, len(polymer))

print(minL)