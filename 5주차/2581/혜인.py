start = int(input())
end = int(input())

num_list = []

for i in range(start, end+1): #+1 해줘야함
    if i < 2:
        continue
    cnt = 0
    for j in range(2, i):
        if(i % j == 0) :
            cnt += 1
            break
    if cnt == 0:
        num_list.append(i)


if sum(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))