def solution(cards1, cards2, goal):
    from collections import deque
    cards1, cards2, goal = deque(cards1), deque(cards2), deque(goal)
    while goal:
        check = goal.popleft()
        if cards1 and cards1[0] == check:
            cards1.popleft()
        elif cards2 and cards2[0] == check:
            cards2.popleft()
        else:
            return "No"
    return "Yes"