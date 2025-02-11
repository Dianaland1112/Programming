cnt = int(input())
x_min, x_max, y_min, y_max = None, None, None, None
for _ in range(cnt):
    x, y = map(int, input().split())
    if not x_min or x_min > x:
        x_min = x
    if not x_max or x_max < x:
        x_max = x
    if not y_min or y_min > y:
        y_min = y
    if not y_max or y_max < y:
        y_max = y
if x_max and x_min and y_min and y_max:
    print((x_max - x_min) * (y_max - y_min))
