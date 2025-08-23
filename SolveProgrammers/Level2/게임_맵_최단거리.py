def solution(maps):
    from collections import deque
    answer = 0
    def move(x, y):
        mov = []
        if x > 0 and maps[y][x - 1] == 1:
            mov.append([x - 1, y])
        if x < len(maps[0]) - 1 and maps[y][x + 1] == 1:
            mov.append([x + 1, y])
        if y > 0 and maps[y - 1][x] == 1:
            mov.append([x, y - 1])
        if y < len(maps) - 1 and maps[y + 1][x] == 1:
            mov.append([x, y + 1])
        return mov
    
    def bfs(node, visited):
        idx = 0
        queue = deque([node])
        visited[node[1]][node[0]] = 1
        while queue:
            node = queue.popleft()
            if node == [len(maps[0]) - 1, len(maps) - 1]:
                return visited[node[1]][node[0]]
            for ele in move(node[0], node[1]):
                if visited[ele[1]][ele[0]] == 1e9:
                    queue.append(ele)
                    visited[ele[1]][ele[0]] = min(visited[ele[1]][ele[0]], visited[node[1]][node[0]] + 1)
        return -1
    visited = [[1e9] * len(maps[0]) for _ in range(len(maps))]
    return bfs([0, 0], visited)