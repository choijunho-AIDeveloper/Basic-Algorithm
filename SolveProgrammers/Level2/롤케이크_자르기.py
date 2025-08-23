def solution(topping):
    from collections import Counter
    answer = 0
    fir = set()
    sec = Counter(topping)
    for top in topping:
        fir.add(top)
        sec[top] -= 1
        if sec[top] == 0:
            del sec[top]
        if len(fir) == len(sec):
            answer += 1
    return answer