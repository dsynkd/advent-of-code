equations = []
try:
    while s := input():
        ss = s.split(':')
        equations.append((int(ss[0]), [int(a) for a in ss[1].strip().split(' ')]))
except EOFError:
    pass

target = 0

def isValid(sum, nums) -> bool:
    if not nums:
        return sum == target
    return isValid(sum + nums[0], nums[1:]) or isValid(sum * nums[0], nums[1:]) or isValid(int(f'{sum}{nums[0]}'), nums[1:])

sum = 0
for eq in equations:
    target = eq[0]
    nums = eq[1]
    if isValid(nums[0], nums[1:]):
        sum += target

print(sum)