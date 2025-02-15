N = int(input())

list_x = []
list_y = []

for _ in range(N):
    x, y = map(int, input().split())
    list_x.append(x)
    list_y.append(y)

width = max(list_x) - min(list_x)
height = max(list_y) - min(list_y)

print(width*height)