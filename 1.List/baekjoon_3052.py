div = 42
test_len = 10
result = []

for i in range(test_len):
    test = int(input())
    rem = test % div
    result.append(rem)

answer = list(set(result))
print(len(answer))

