def solution(k, score):
    import heapq
    li = []
    answer = []
    for i in range(len(score)):
        if i < k:
            heapq.heappush(li, score[i])
            answer.append(li[0])
        else:
            if li[0] < score[i]:
                heapq.heappop(li)
                heapq.heappush(li, score[i])
            answer.append(li[0])
            
    return answer