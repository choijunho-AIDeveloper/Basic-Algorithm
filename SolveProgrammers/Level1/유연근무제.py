def solution(schedules, timelogs, startday):
    answer = 0
    for i, timelog in enumerate(timelogs):
        isCheck = False
        can = schedules[i] + 10
        if can % 100 >= 60:
            can = (can // 100 + 1) * 100 + (can % 100 - 60)
        for log in timelog:
            if startday not in [6, 7]:
                if log > can:
                    isCheck = True
            startday += 1
            if startday > 7:
                startday = 1
        if not isCheck:
            answer += 1
                    
    return answer