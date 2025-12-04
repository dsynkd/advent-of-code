positions = [int(a) for a in input().split(',')]
m = max(positions)

minCost = float('inf')

dp = [[-1 for _ in range(m+1)] for _ in range(m+1)]

for i in range(m+1):
    cost = 0
    for p in positions:
        s = sum(range(abs(p-i)+1))
        cost += abs(s)
    minCost = min(minCost, cost)

print(minCost)