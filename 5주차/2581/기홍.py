def dec(num):
    select = 0
    for i in range(2, num):
        if num % i == 0:
            select = 1
            break
    if num == 1:
        return 1
    return select


def min1(a, b):
    min = 0
    for i in range(a, b + 1):
        if dec(i) == 0:
            min = i
            break
    return min


min = int(input())
max = int(input())
sum = 0
for i in range(min, max + 1):
    if dec(i) == 0:
        sum = sum + i
print(f"{sum}\n{min1(min,max)}" if sum else -1)
