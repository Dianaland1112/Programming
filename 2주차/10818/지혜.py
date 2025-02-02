# 첫 번째 줄: 정수의 개수 입력
N = int(input())  # N은 1 이상 1,000,000 이하로 주어짐

# 두 번째 줄: N개의 정수를 공백으로 입력받아 문자열 리스트로 저장
numbers_input = input().split()

# 문자열 리스트를 정수 리스트로 변환
numbers = []
for num in numbers_input:
    numbers.append(int(num))

# 1. 최소값과 최대값을 리스트의 첫 번째 값으로 초기화
min_value = numbers[0]
max_value = numbers[0]

# 2. 리스트를 순회하면서 최소값과 최대값 갱신
for num in numbers:
    if num < min_value: # 현재 숫자가 최소값보다 작다면
        min_value = num # 최소값을 현재 숫자로 갱신
    if num > max_value: # 현재 숫자가 최대값보다 크다면
        max_value = num # 최대값을 현재 숫자로 갱신

# 결과 출력
print(min_value, max_value)
