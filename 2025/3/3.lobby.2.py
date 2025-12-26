res = 0
joltage_length = 12

for line in open(0):
    bank = list(map(int, line.strip()))
    bank_length = len(bank)
    joltage = ''

    for i in range(joltage_length):
        offset = i - joltage_length + 1
        if offset == 0:
            offset = bank_length
        
        digit = max(bank[:offset])
        bank = bank[bank.index(digit) + 1:]
        joltage += str(digit)
    
    res += int(joltage)

print(res)