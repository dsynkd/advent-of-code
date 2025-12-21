res = 0

for line in open(0):
    bank = list(map(int, line.strip()))
    # Find max joltage
    m1 = max(bank[:-1])
    m2 = max(bank[bank.index(m1) + 1:])
    res += int(f'{m1}{m2}')

print(res)