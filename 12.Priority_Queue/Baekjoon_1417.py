# 후보자들
n = int(input())

# 득표 수
n_list = [0] * n

for i in range(n):
    inp = int(input())
    n_list[i] = inp

n_list.reverse()
    
max_n = max(n_list)
max_index = n_list.index(max_n)

count = 0

while max_index != n - 1:
    count += 1
    n_list[max_index] -= 1
    n_list[-1] += 1

    max_n = max(n_list)
    max_index = n_list.index(max_n)

    if max_index == n - 1:
        break


print(count)