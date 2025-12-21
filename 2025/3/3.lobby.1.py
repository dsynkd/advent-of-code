res = 0

for line in open(0):
    bank = list(map(int, line.strip()))

    digit1 = max(bank[:-1])
    digit2 = max(bank[bank.index(digit1) + 1:])

    res += int(f'{digit1}{digit2}')

print(res)