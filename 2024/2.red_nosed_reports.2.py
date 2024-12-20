import copy

reports = []
while True:
    try:
        s = input().split(' ')
        reports.append([int(a) for a in s])
    except EOFError:
        break

def is_safe(levels: list[int]) -> bool:
    direction = 1 if levels[1] - levels[0] > 0 else 0
    
    for i in range(1, len(levels)):
        level = levels[i]
        prev_level = levels[i-1]
        diff = level - prev_level
        cur_direction = 1 if diff > 0 else 0
        if cur_direction != direction or not (1 <= abs(diff) <= 3):
            return False

    return True    

safety = 0
for i in range(len(reports)):
    levels = reports[i]
    if is_safe(levels):
        safety += 1
    else:
        for j in range(len(levels)):
            levels_copy = levels.copy()
            levels_copy.pop(j)
            if is_safe(levels_copy):
                safety += 1
                break

print(safety)