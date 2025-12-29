intervals = []
fd = open(0)

for line in fd:
    line = line.strip()
    if not line:
        break
    intervals.append(list(map(int, line.strip().split('-'))))

intervals.sort()
merged_intervals = [intervals[0]]

for i in range(1, len(intervals)):
    cur = intervals[i]
    last = merged_intervals[-1]
    if cur[0] > last[1]:
        merged_intervals.append(cur)
    else:
        last[1] = max(cur[1], last[1])

res = 0
for i,j in merged_intervals:
    res += j-i+1

print(res)