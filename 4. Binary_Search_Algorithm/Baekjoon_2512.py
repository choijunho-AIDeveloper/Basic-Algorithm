n = int(input())
budget = list(map(int, input().split()))
max_possible_budget = int(input())

max_budget, min_budget = max(budget), 0

result = 0

while max_budget >= min_budget:
    mid = (max_budget + min_budget)//2
    new_budget = budget[:]
    for i in range(len(new_budget)):
        if new_budget[i] > mid:
            new_budget[i] = mid
    total = sum(new_budget)
    if total <= max_possible_budget:
        result = mid
        min_budget = mid + 1
    else:
        max_budget = mid - 1

print(result)