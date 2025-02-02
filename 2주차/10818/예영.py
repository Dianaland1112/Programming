n = int(input())
nums = list(map(int, input().split()))
max_num = nums[0]
min_num = nums[0]
for i in nums:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i

print(min_num, max_num)
