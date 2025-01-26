n = int(input())
n_list = list(map(int, input().split()))

n_list.sort()

sum = 0
sum_point = 0
for i in range(len(n_list)):
    sum_point += n_list[i]
    sum += sum_point

print(sum)