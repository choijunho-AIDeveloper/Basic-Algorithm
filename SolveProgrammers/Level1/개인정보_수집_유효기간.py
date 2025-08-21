def solution(today, terms, privacies):
    from collections import defaultdict
    check = []
    result = []
    termDict = defaultdict()
    for term in terms:
        fir, sec = term.split()
        termDict[fir] = int(sec)
    todYear, todMon, todDay = today.split(".")
    for i, privacy in enumerate(privacies):
        fir, sec = privacy.split()
        year, mon, day = fir.split(".")
        year = int(year) + (int(mon) + termDict[sec]) // 12
        mon = (int(mon) + termDict[sec]) % 12
        if mon == 0:
            mon = 12
            year -= 1
        day = int(day)
        day -= 1
        if day == 0:
            mon -= 1
            if mon == 0:
                mon = 12
            day = 28
        if (year > int(todYear)) or (year == int(todYear) and mon > int(todMon)) or (year == int(todYear) and mon == int(todMon) and day >= int(todDay)):
            pass
        else:
            result.append(i + 1)
            
            
    return result