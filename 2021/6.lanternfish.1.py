state = [int(a) for a in input().split(',')]
N = 80

while N > 0:
    for i in range(len(state)):
        n = state[i]
        if n == 0:
            state[i] = 6
            state.append(8)
        else:
            state[i] -= 1
    N -= 1

print(len(state))