from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

max_result = - 1
for i in permutations(a):
    sum = 0
    for j in range(len(i) - 1):
        sum += abs(i[j] - i[j + 1])
    if sum > max_result:
        max_result = sum

print(max_result)