# 첫 번째 줄: N과 M 입력
input_line = input().split()  # 첫 줄 입력받기
N = int(input_line[0])  # 바구니 개수
M = int(input_line[1])  # 공을 넣는 방법 개수

# 바구니 초기화: N개의 바구니를 0으로 초기화
baskets = [0] * N

# 공 넣기 방법 처리
for _ in range(M):
    # i, j, k 입력받기
    method = input().split()  # 공 넣기 방법 입력받기
    i = int(method[0])  # 시작 바구니
    j = int(method[1])  # 끝 바구니
    k = int(method[2])  # 넣을 공 번호

    # i번째부터 j번째 바구니까지 공 번호 k를 넣기
    for idx in range(i - 1, j):  # 리스트는 0부터 시작하므로 i-1부터 j-1까지
        baskets[idx] = k

# 최종 바구니 상태 출력
result = ''  # 출력 문자열 초기화
for value in baskets:  # 바구니 리스트의 모든 값을 순회
    result += str(value) + ' '  # 각 값을 문자열로 변환하고 공백을 추가
print(result)
