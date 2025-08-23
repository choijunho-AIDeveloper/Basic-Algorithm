def solution(elements):
    num_list = set()
    circle = elements + elements[:-1]
    for i in range(1, len(elements) + 1):
        for j in range(len(circle) - i + 1):
            num_list.add(sum(circle[j:j+i]))
    return len(num_list)