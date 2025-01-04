div_num = 42
test_len = 10
result_list = []

for i in range(test_len):
    test_num = int(input())
    rem = test_num % div_num
    result_list.append(rem)

answer = list(set(result_list))
print(len(answer))

