def solution(scoville, K):
    import heapq
    answer = 0
    queue = []
    for ele in scoville:
        heapq.heappush(queue, ele)
    fir = heapq.heappop(queue)
    sec = heapq.heappop(queue)
    while fir < K:
        answer += 1
        new = fir + sec * 2
        if len(queue) == 0:
            if new < K:
                return -1
            else:
                heapq.heappush(queue, new)
                break
        heapq.heappush(queue, new)
        fir = heapq.heappop(queue)
        sec = heapq.heappop(queue)
    heapq.heappush(queue, fir)
    heapq.heappush(queue, sec)
    return answer