def solution(N, stages):
    stages.sort()
    prev = 0
    stageMap = [0] * (N + 1)
    for ele in stages:
        stageMap[ele - 1] += 1
    prev = 0
    for ele in range(len(stageMap)):
        if len(stages) - prev > 0:
            temp = stageMap[ele]
            print((len(stages) - prev), stageMap[ele])
            stageMap[ele] = stageMap[ele]/(len(stages) - prev)
            prev += temp
        else:
            stageMap[ele] = 0
    stageMap.pop()
    result = sorted(list(range(N)), key = lambda x : stageMap[x], reverse = True)
    return [i + 1 for i in result]