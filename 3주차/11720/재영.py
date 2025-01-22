N = int(input()) #문자열 개수 입력
a = input() #문자열 입력
list = [] #각 자리수 넣을 리스트 설정정
for i in range(N): 
    list.append(int(a[i])) # a를 각각 나누어 list에 넣기기
print(sum(list)) # list 총 합 출력