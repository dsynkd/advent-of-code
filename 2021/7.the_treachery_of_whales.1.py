positions = [int(a) for a in input().split(',')]
m = max(positions)

minCost = float('inf')

for i in range(0, m+1):
    cost = 0
    for p in positions:
        cost += abs(p-i)
    minCost = min(minCost, cost)

print(minCost)