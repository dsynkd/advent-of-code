prev_depth = None
count = 0

while(True):
    try:
        depth = int(input())
    except:
        break
    if prev_depth is not None and depth > prev_depth:
        count += 1
    prev_depth = depth

print(count)