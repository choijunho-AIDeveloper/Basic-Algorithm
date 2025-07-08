from collections import deque

result = []
while True:
    testcase = input()
    if testcase == ".":
        break
    stack = deque()
    false_stack = False
    for i in range(len(testcase)):
        if testcase[i] == "(" or testcase[i] == "[" or testcase[i] == ")" or testcase[i] == "]":
            if testcase[i] == "(" or testcase[i] == "[":
                stack.append(testcase[i])
            else:
                if testcase[i] == ")" and len(stack) == 0:
                    false_stack = True
                    break
                elif testcase[i] == ")" and stack[-1] == "(" and len(stack) > 0:
                    stack.pop()
                elif testcase[i] == "]" and len(stack) == 0:
                    false_stack = True
                    break
                elif testcase[i] == "]" and stack[-1] == "[" and len(stack) > 0:
                    stack.pop()
                else:
                    break
    # ")", "]"로 시작 case
    if false_stack == True:
        result.append("no")
        continue
    # 완전히 닫힌 case
    if len(stack) == 0:
        result.append("yes")
    # 닫히지 않은 case
    else:
        result.append("no")

for i in range(len(result)):
    print(result[i])


