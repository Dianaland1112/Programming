try:
    # 입력받기
    input_value = input()  # 문제에서 추가 출력은 금지될 가능성이 있으므로 메시지 제거

    # 입력값이 정확히 하나인지 확인
    if len(input_value.split()) > 1:
        exit()  # 여러 개 입력된 경우 추가 출력 없이 종료
    else:
        # 입력값을 정수로 변환
        N = int(input_value)

        # 입력값이 조건을 만족하는지 확인
        if 4 <= N <= 1000 and N % 4 == 0:
            # "long" 반복 횟수 계산
            repeat_count = N // 4
            # 출력 결과 생성
            result = "long " * repeat_count + "int"
            # 결과 출력
            print(result)
        else:
            exit()  # 조건을 만족하지 않으면 추가 출력 없이 종료
except:
    exit()  # 오류 발생 시 추가 출력 없이 종료
