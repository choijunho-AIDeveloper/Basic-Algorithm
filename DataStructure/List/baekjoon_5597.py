student_num = 30
non_submit = 2

empty_list = [0] * student_num

for i in range(len(empty_list) - non_submit):
    submit = int(input())
    empty_list[submit - 1] = 1

for i in range(len(empty_list)):
    if empty_list[i] == 0:
        print(i + 1)