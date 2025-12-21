res = 0

for line in open(0):
    bank = list(map(int, line.strip()))
    # Find max joltage
    jolt = ''
    for i in range(11):
        digit = max(bank[:i - 11])
        bank = bank[bank.index(digit) + 1:]
        jolt += str(digit)
    print('jolt:', jolt)
    res += int(jolt)

print(res)