from collections import deque
import sys

commands = int(input())
queue = deque()

result_list = []

for i in range(commands):
    command = sys.stdin.readline()
    command = command.split()
    if command[0] == "push":
        queue.append(command[1])
    if command[0] == "pop":
        if len(queue) == 0:
            result_list.append(-1)
            continue
        result_list.append(queue.popleft())
    if command[0] == "size":
        result_list.append(len(queue))
    if command[0] == "empty":
        if len(queue) == 0:
            result_list.append(1)
        else:
            result_list.append(0)
    if command[0] == "front":
        if len(queue) == 0:
            result_list.append(-1)
            continue
        result_list.append(queue[0])
    if command[0] == "back":
        if len(queue) == 0:
            result_list.append(-1)
            continue
        result_list.append(queue[-1])

for result in result_list:
    print(result)
