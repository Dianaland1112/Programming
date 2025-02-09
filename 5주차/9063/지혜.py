N = int(input()) # 점의 개수 입력

min_x, max_x = 10000, -10000 # 초기값 설정하여 업데이트 통해 최소/최대 갱신
min_y, max_y = 10000, -10000

for i in range(N): # 점의 좌표 입력하여 최소/최대 갱신
    x, y = map(int, input().split())
        
    if x < min_x: # x좌표의 최소/최대값 갱신
        min_x = x
    if x > max_x:
        max_x = x

    if y < min_y: # y좌표의 최소/최대값 갱신
        min_y = y
    if y > max_y:
        max_y = y

area = (max_x - min_x) * (max_y - min_y) # 직사각형의 넓이 계산

print(area)
