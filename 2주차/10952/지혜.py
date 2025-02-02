while True:
    # 두 정수를 입력받아 공백 기준으로 나눔
    input_line = input().split()
    
    # 문자열로 입력된 값을 정수로 변환해야 사칙연산 가능
    A = int(input_line[0])
    B = int(input_line[1])
    
    # 종료 조건: 0 0 이 입력되면 종료
    if A == 0 and B == 0:
        break
    
    # A + B 출력
    print(A + B)
