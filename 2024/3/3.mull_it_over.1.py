sections = []
try:
    while s := input():
        sections.append(s)
except:
    pass

product = 0
for section in sections:
    i = 0
    while i < len(section):
        if section[i:i+4] == "mul(":
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
        else:
            i += 1

print(product)