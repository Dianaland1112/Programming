arr = []
max_val = -1 # 입력값 모두 0인 경우 고려
max_i = 0
max_j = 0

for i in range(9):
    n = list(map(int, input().split()))
    arr.append(n)

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            max_i = i+1
            max_j = j+1
            
print(max_val)
print(max_i, max_j)