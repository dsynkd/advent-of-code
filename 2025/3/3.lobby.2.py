res = 0
n = 12

for line in open(0):
    bank = list(map(int, line.strip()))
    joltage = ''

    for i in range(1,n):
        offset = i - n
        digit = max(bank[:offset])
        bank = bank[bank.index(digit) + 1:]
        joltage += str(digit)
    
    res += int(joltage)

print(res)