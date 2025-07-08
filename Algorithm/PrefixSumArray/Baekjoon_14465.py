import sys

input = sys.stdin.readline

n, k = map(int, input().split())
n_list = list(map(int, input().split()))

current_sum = sum(n_list[:k])
max_sum = current_sum

for i in range(n - k):
    current_sum = current_sum - n_list[i] + n_list[i + k]
    max_sum = max(max_sum, current_sum)


print(max_sum)