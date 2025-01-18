import sys

t = int(sys.stdin.readline())

results = []

for _ in range(t):
    failed = 0
    candidates = []
    point = 10 ** 9
    n = int(sys.stdin.readline())
    for _ in range(n):
        candidate = list(map(int, sys.stdin.readline().split()))
        candidates.append(candidate)
    candidates.sort()
    for j in range(len(candidates)):
        if point > candidates[j][1]:
            point = candidates[j][1]
        else:
            failed += 1
    results.append(len(candidates) - failed)

for result in results:
    print(result)