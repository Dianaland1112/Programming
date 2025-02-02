# 숫자를 입력받습니다.
n = input().strip()  # 숫자를 문자열로 입력받습니다.

# 자릿수를 내림차순으로 정렬합니다.
sorted_digits = sorted(n, reverse=True)  # 큰 숫자부터 작은 숫자 순으로 정렬합니다.

# 정렬된 숫자들을 합쳐 하나의 문자열로 만듭니다.
result = ''.join(sorted_digits)

# 결과를 출력합니다.
print(result)  # 정렬된 숫자를 출력합니다.
