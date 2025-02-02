# 입력
N = int(input())  # 첫 번째 줄: 정수의 개수
numbers = input().split()  # 두 번째 줄: 공백으로 구분된 N개의 정수
v = int(input())  # 세 번째 줄: 찾으려는 정수 v

# 문자열 리스트를 정수 리스트로 변환
int_numbers = []
for num in numbers:
    int_numbers.append(int(num))

# v의 개수 세기
count = 0
for num in int_numbers:
    if num == v:
        count += 1

# 출력
print(count)
