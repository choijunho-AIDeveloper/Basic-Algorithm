def solution(number):
    from itertools import combinations
    
    canList = list(combinations(number, 3))
    
    return len([ele for ele in canList if sum(ele) == 0])