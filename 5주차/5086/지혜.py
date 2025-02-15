A, B = map(int, input().split())  

while A != 0 or B != 0:
    if B % A == 0:
        print("factor")  # 약수면
    elif A % B == 0:
        print("multiple")  # 배수면
    else:
        print("neither")  # 둘 다 아니면

    A, B = map(int, input().split())  # 반복문 안에서 다음 입력 받기
