import sys

input = sys.stdin.readline

n, k, b = map(int, input().split())

b_list = [0] * n

for i in range(b):
    input_num = int(input())
    b_list[input_num - 1] = 1

current = sum(b_list[:k])
result = current

for i in range(n - k):
    current = current - b_list[i] + b_list[i + k]
    result = min(current, result)

print(result)