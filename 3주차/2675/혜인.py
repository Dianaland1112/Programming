a = int(input())
for _ in range(a):
    b, c = input().split() #같은 줄에 있으므로 split으로 입력받음
    for i in range(len(c)):
        print(c[i]*int(b), end='') #한줄에 여러개 입력하려면 end= '' 필요
    print('') #한 칸 띄워줘야 다음 값 입력받을 수 있음 
