# 입력 받기
N, M = input().split()  # 바구니 개수 N, 뒤집기 작업 M
N = int(N)
M = int(M)

buckets = list(range(1, N + 1))  # 1부터 N까지 번호가 적힌 바구니 생성

# M번의 뒤집기 작업 수행
for _ in range(M):
    i, j = input().split()
    i = int(i)
    j = int(j)
    # i부터 j까지의 범위를 뒤집기
    buckets[i - 1:j] = buckets[i - 1:j][::-1]

# 결과 출력
result = ""
for num in buckets:
    result += str(num) + " "
print(result)
