import heapq


n = int(input())
n_list = []

for i in range(n):
    inp = int(input())
    heapq.heappush(n_list, inp)

result = 0

while len(n_list) > 1:
    num1 = heapq.heappop(n_list)
    num2 = heapq.heappop(n_list)
    sum_num = num1 + num2

    result += sum_num

    heapq.heappush(n_list, sum_num)

print(result)
