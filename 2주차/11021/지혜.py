# 첫 줄: 테스트 케이스 개수 입력
try:
    T = int(input())  # 테스트 케이스 수 입력
except ValueError:
    print("테스트 케이스 수는 정수여야 합니다.")
    exit()  # 프로그램 종료

# 각 테스트 케이스 처리
for i in range(1, T + 1):
    try:
        # A, B 입력받기
        input_list = input().split()

        # 입력값이 2개인지 확인
        if len(input_list) != 2:
            print("두 개의 정수를 입력해야 합니다.")
            continue

        # 각 정수로 변환
        A = int(input_list[0])  # 첫 번째 값 변환
        B = int(input_list[1])  # 두 번째 값 변환

        # A, B 조건 검사 (0 < A, B < 10)
        if 0 < A < 10 and 0 < B < 10:
            print(f"Case #{i}: {A + B}")
        else:
            print("A와 B는 1 이상 9 이하여야 합니다.")
    except ValueError:
        print("A와 B는 정수여야 합니다.")
