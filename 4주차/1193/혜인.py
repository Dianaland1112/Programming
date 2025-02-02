# 1/1
# 1/2, 2/1
# 3/1, 2/2, 1/3
# 1/4, 2/3, 3/2, 4/1
# 5/1, 4/2, 3/3, 2/4, 1/5
count = 1
input1 = int(input())
while input1 - count > 0 :
    input1 -= count
    count += 1

if count % 2 == 0:
    print(f"{input1}/{count - input1 + 1}")
else:
    print(f"{count - input1 + 1}/{input1}")  



