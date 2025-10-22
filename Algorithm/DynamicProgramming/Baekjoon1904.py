n = int(input())

dpMap = [0] * (n+1)

if len(dpMap)>=2: dpMap[1] = 1
if len(dpMap)>=3: dpMap[2] = 2

for i in range(3, len(dpMap)):
    dpMap[i] = (dpMap[i-1] + dpMap[i-2])%15746

print(dpMap[n])