import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a_num, b_num = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    a_po = 0
    b_po = 0
    sum = 0


    while a_po < a_num:
        if a[a_po] > b[b_po]:
            b_po += 1
            if b_po == b_num:
                sum += (a_num - a_po) * b_num
                break
        else:
            sum += b_po
            a_po += 1
    print(sum)