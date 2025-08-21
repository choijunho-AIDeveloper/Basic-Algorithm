def solution(phone_number):
    change = 0
    phone_number = list(phone_number)
    for i in range(len(phone_number) - 1, -1, -1):
        if change == 4:
            phone_number[i] = "*"
        else:
            change += 1
    return "".join(phone_number)