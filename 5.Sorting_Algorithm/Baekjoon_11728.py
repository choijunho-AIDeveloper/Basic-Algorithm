a_size, b_size = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.extend(b)
a.sort()
result = list(map(str, a))

print(" ".join(result))