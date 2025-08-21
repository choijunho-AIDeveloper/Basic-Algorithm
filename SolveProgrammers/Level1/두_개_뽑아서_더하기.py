def solution(numbers):
    from itertools import combinations
    
    numList = list(set([sum(ele) for ele in combinations(numbers, 2)]))
    numList.sort()
    
    return numList