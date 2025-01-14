from collections import deque

def is_valid(le_list, target, m):
    le_list = deque(le_list)
    for i in range(m):
        sum = 0
        while len(le_list) > 0:
            if sum + le_list[0] > target:
                break
            else:
                sum += le_list[0]
                le_list.popleft()
    if len(le_list) > 0:
        return False
    else:
        return True

n, m = map(int, input().split())
lesson_list = list(map(int, input().split()))

min, max = max(lesson_list), sum(lesson_list)
result = 0
while max >= min:
    mid = (max + min) // 2
    if is_valid(lesson_list, mid, m):
        result = mid
        max = mid - 1
    else:
        min = mid + 1

print(result)
        