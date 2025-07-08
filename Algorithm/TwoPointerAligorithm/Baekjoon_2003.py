import sys

n, m = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
result = 0
sum = a[0]

while start < n:
    if sum == m:
        result += 1
        sum -= a[start]
        start += 1
    elif sum < m:
        end += 1
        if end == n:
            break
        sum += a[end]
    elif sum > m:
        sum -= a[start]
        start += 1


print(result)