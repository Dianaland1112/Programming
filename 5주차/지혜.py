A = int(input()) #input 함수는 항상 문자열로 값을 반환 -> 숫자 입력해도 문자열로 인식
B = int(input())

if 1 <= A <= 100 and 1 <= B <= 100:
    area = A * B # 조건 만족하면 넓이 계산하여 출력
    print(area)
else:
    print("A와 B는 1 이상 100 이하의 정수여야 한다.")  
