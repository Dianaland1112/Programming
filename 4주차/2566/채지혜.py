##최대값을 찾기 위해 모든 원소를 순회한다.
matrix = [] # 9개의 줄에서 입력받은 숫자를 저장할 리스트를 만든다.

for i in range(9): # 9번 반복해서 입력 받기
 row = [int(num) for num in input().split()]  # 한 행을 입력받고, 숫자로 변환해 리스트로 저장, 공백을 기준으로 구분문자열을 숫자 리스트로 변환
 matrix.append(row) # 숫자 리스트를 행렬에 추가
 
max_value = matrix[0][0] # 행렬의 첫 번째 원소로 초기값 설정
max_row = 1 #최댓값 행 번호(1부터 시작)
max_col = 1 #열 번호(1부터 시작)

for i in range(9): # 모든 행을 순회하며 최대값의 위치 찾기
    for j in range(9): # 각 행의 모든 열을 순회
        if matrix[i][j] > max_value: # 현재 위치의 숫자가 지금까지 찾은 최대값보다 크면,
            max_value = matrix[i][j] #최대값을 현재 위치의 숫자로 갱신
            max_row = i + 1  # 최대값의 행 번호(컴퓨터는 0부터 세지만, 사람은 1부터 세서 +1)
            max_col = j + 1  # 최대값의 열 번호

# 결과 출력
print(max_value)
print(max_row, max_col)
