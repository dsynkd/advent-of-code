res = 0

nums = {'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9}

for line in open(0):
    line = line.strip()
    val = ''

    for i in range(len(line)):
        if line[i].isdigit():
            val += line[i]
            break
        else:
            for n in nums.keys():
                sub = line[i:min(len(line)-1, i+len(n))]
                if sub == n:
                    val += str(nums[n])
                    break
            if val:
                break
    
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            val += line[i]
            break
        else:
            for n in nums.keys():
                sub = line[max(0, i+1-len(n)):i+1]
                if sub == n:
                    val += str(nums[n])
                    break
        if len(val) > 1:
            break
    
    res += int(val)

print(res)