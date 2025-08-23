def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    while left <= right:
        answer += 1
        
        curWeight = people[right]
        right -= 1
        
        if curWeight + people[left] <= limit:
            left += 1
    return answer