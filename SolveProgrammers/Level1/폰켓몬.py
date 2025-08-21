def solution(nums):
    from collections import Counter
    nDict = Counter(nums)
    return min(len(nDict), len(nums)//2)