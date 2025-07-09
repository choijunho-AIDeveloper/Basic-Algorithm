# 1446
import heapq

n, m = map(int, input().split())
INF = 1e9

# 그래프 생성
graph = [[] for _ in range(m + 1)]

# 지름길 넣기
for _ in range(n):
    start, end, length = map(int, input().split())
    if end <= m:
        graph[start].append([end, length])

# 그냥 길 넣기
for i in range(m):
    graph[i].append([i + 1, 1])

# distance 초기화
distance = [INF] * (m + 1)
distance[0] = 0


queue = [[0, 0]]
while queue:
    # 같은 출발점에 있을 경우
    dist, node = heapq.heappop(queue)

    if dist > distance[node]:
        continue

    # distance 업데이트
    for neighbor, weight in graph[node]:
        new_dist = dist + weight
        # 현재 목표 위치의 시간과 업데이트할 시간을 비교
        if new_dist < distance[neighbor]:
            distance[neighbor] = new_dist
            heapq.heappush(queue, (new_dist, neighbor))

print(distance[m])