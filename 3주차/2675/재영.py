T = int(input()) #케이스 입력
for i in range(T): #케이스 만큼 반복
    a,S = map(str,input().split()) # R,S를 입력
    R = int(a) #R을 정수로 받을 수 있게 바꿈
    result = '' #결과값 설정
    for j in list(S):
        result+= j*R #각 자리를 R번 곱한것만큼 결과값에 적용용
    print(result)

