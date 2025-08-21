def solution(a, b):
    monthMap = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    datMap = {0 :"SUN", 1 : "MON", 2 : "TUE", 3 : "WED", 4 : "THU", 5 : "FRI", 6 : "SAT"}
    return datMap[(sum(monthMap[:a]) + b + 4) % 7]