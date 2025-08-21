def solution(lottos, win_nums):
    curCorrect = []
    answer = [0, 0]
    cantNum = len(win_nums)
    zeroNum = 0
    
    def changeNum(num):
        change = 0
        if num == 6:change = 1
        elif num == 5:change = 2
        elif num == 4:change = 3
        elif num == 3:change = 4
        elif num == 2:change = 5
        else:change = 6
        return change
    
    for lotto in lottos:
        if lotto == 0:
            zeroNum += 1
        else:
            if lotto in win_nums:
                answer[0], answer[1] = answer[0] + 1, answer[1] + 1
                cantNum -= 1
    answer[0] += min(cantNum, zeroNum)
    
    return [changeNum(answer[0]), changeNum(answer[1])]
