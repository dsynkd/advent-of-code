equations = []
try:
    while s := input():
        ss = s.split(':')
        equations.append((int(ss[0]), [int(a) for a in ss[1].strip().split(' ')]))
except EOFError:
    pass

def isValid(target, sum, nums) -> bool:
    if not nums:
        return sum == target
    return isValid(target, sum + nums[0], nums[1:]) or isValid(target, sum * nums[0], nums[1:])

sum = 0
for eq in equations:
    target = eq[0]
    nums = eq[1]
    if isValid(target, nums[0], nums[1:]):
        sum += target

print(sum)