t = int(input())
cnt_list = [[] for _ in range(t)]
for rpt in range(t):
    c = int(input())
    _list = [25, 10, 5, 1]
    for i in range(4):
        cnt_list[rpt].append(c // _list[i])
        c = c % _list[i]
for result in cnt_list:
    print(*result)
