a = input().upper()  # 모두 소문자로

b = list(set(a))  # 중복 제거하기
c = []

for i in b:
    count = a.count(i)  # 각 알파벳이 몇 번 나오는지 세기
    c.append(count)


    if c.count(max(c)) >= 2:  # 가장 큰 값이 2개 이상이면 ?
        print("?")
    else: 
        print(b[c.index(max(c))])  # 제일 많이 나온 알파벳 출력
