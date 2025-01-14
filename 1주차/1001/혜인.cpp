try :
    # 입력받기
    input_value = input().strip()

    # 입력값이 정확히 하나의 숫자인지 확인
    if len(input_value.split()) > 1:
print("입력 값이 너무 많습니다. 하나의 숫자만 입력해주세요.")
    else:
N = int(input_value)

# 입력값이 조건을 만족하는지 확인
if 1 <= N <= 9:
# 구구단 출력
for i in range(1, 10) :
    print(f"{N} * {i} = {N * i}")
else:
# 입력값이 조건에 맞지 않을 때
print("입력 값이 조건을 만족하지 않습니다. N은 1 이상 9 이하의 정수여야 합니다.")
except ValueError :
# 입력값이 정수가 아닌 경우
print("유효하지 않은 입력입니다. 정수를 입력해주세요.")