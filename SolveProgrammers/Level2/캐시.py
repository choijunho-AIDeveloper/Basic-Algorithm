def solution(cacheSize, cities):
    from collections import deque
    answer = 0
    cityList = deque(maxlen = cacheSize)
    for city in cities:
        city = city.lower()
        if city in cityList:
            cityList.remove(city)
            cityList.append(city)
            answer += 1
        else:
            cityList.append(city)
            answer += 5
    return answer