sections = []
try:
    while s := input():
        sections.append(s)
except:
    pass

product = 0
active = True
for section in sections:
    i = 0
    while i < len(section):
        if section[i:i+4] == "mul(" and active:
            i += 4
            arg1 = ""
            j = i
            while j-i < 4 and section[j] != ',':
                arg1 += section[j]
                j += 1
            if section[j] != ',':
                continue
            i = j+1
            arg2 = ""
            j = i
            while j-i < 4 and section[j] != ')':
                arg2 += section[j]
                j += 1
            if section[j] != ')':
                continue
            product += int(arg1) * int(arg2)
            i = j + 1
        elif section[i:i+7] == "don't()":
            active = False
            i += 7
        elif section[i:i+4] == "do()":
            active = True
            i += 4
        else:
            i += 1

print(product)