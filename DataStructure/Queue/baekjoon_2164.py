from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    queue.append(i + 1)

change = False
while len(queue) > 1:
    if change == False:
        queue.popleft()
        change = True
    elif change == True:
        toBack = queue.popleft()
        queue.append(toBack)
        change = False

print(queue[0])

from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    queue.append(i + 1)

while len(queue) > 1:
    queue.popleft()
    toBack = queue.popleft()
    queue.append(toBack)

print(queue[0])