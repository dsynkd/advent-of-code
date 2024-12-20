#!/usr/bin/python3

import fileinput

depths = []
sums = []
count = 0

while(True):
    try:
        depth = int(input())
    except:
        break
    depths.append(depth)

for i in range(0,len(depths)-2):
    sums.append(depths[i] + depths[i+1] + depths[i+2])

for i in range(1,len(sums)):
    if sums[i] > sums[i-1]:
        count += 1

print(count)
