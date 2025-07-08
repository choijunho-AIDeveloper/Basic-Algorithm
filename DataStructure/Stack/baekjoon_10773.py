from collections import deque

k = int(input())
stack = deque()

for i in range(k):
    testcase = int(input())
    if testcase == 0:
        stack.pop()
    else:
        stack.append(testcase)

print(sum(stack))
