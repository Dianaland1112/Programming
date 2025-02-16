a, b, c = map(int, input().split())

while a != 0 or b != 0 or c != 0: #a,b,c 중 하나라도 0이 아니면 반복한다
    if a + b <= c or a + c <= b or b + c <= a: # 가장 긴 변 < 나머지 두 변의 합
        print("Invalid")
    else:
        if a == b == c: # 세 변의 길이가 모두 같으면 
            print("Equilateral")
        elif a == b or b == c or a == c: # 두변의 길이만 같으면 
            print("Isosceles")
        else: # 세 변의 길이가 모두 다르면 
            print("Scalene")

    # 다음 입력 받기
    a, b, c = map(int, input().split())
