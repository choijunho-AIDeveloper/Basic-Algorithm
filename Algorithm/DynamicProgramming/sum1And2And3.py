# 9095
n = int(input())

# 1, 2, 3 Least Common Multiple + 1
# 최소공배수로 구할 수 있을까?
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)

possibleMap = [0] * (max(nums) + 1)
possibleMap[0] = 1
possibleMap[1] = 1
possibleMap[2] = 2

for i in range(3, len(possibleMap)):
    possibleMap[i] = possibleMap[i - 3] + possibleMap[i - 2] + possibleMap[i - 1]

for i in range(len(nums)):
    print(possibleMap[nums[i]])