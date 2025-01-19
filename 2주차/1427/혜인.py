num = int(input())
l = list(map(int,str(num)))
l.sort(reverse=True)

for i in l:
    print(i, end='')