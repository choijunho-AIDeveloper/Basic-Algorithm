n = int(input())
n_list = []

for _ in range(n):
    input_num = int(input())
    n_list.append(input_num)

n_list.reverse()
result = 0
for i in range(len(n_list) - 1):
    if n_list[i + 1] >= n_list[i]:
        result += n_list[i + 1] - n_list[i] + 1
        n_list[i + 1] = n_list[i] - 1

print(result)