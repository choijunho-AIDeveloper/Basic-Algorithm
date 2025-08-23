def solution(priorities, location):
    import heapq
    li = []
    for i in range(len(priorities)):
        heapq.heappush(li, -priorities[i])
    idx = 0
    visited = [False] * len(priorities)
    for i in range(len(priorities)):
        temp = -heapq.heappop(li)
        while visited[idx] or temp != priorities[idx]:
            idx += 1
            if idx == len(priorities):
                idx = 0
        if idx == location:
            return i + 1
        visited[idx] = True