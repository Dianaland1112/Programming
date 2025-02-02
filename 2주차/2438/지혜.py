# 첫 줄: 정수 N 입력받기
try:
    N = int(input())
    if 1 <= N <= 100:
        # 1부터 N까지 반복하며 각 줄 출력
        for i in range(1, N + 1):
            print("*" * i)  # i개의 '*' 출력
    else:
        print("N은 1 이상 100 이하의 정수여야 합니다.")
except ValueError:
    print("정수를 입력해야 합니다.")
