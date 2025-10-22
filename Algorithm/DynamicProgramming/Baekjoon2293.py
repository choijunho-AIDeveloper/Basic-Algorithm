n, k = map(int, input().split())

n_list = []
dpMap = [0] * (10001)
for _ in range(n):
    temp = int(input())
    n_list.append(temp)
dpMap[0] = 1

for num in n_list:
    for i in range(num, k+1):
        dpMap[i] = dpMap[i] + dpMap[i-num]

print(dpMap[k])