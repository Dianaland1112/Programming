x, y = [0, 0, 0], [0, 0, 0]
for i in range(3):
    x[i], y[i] = map(int, input().split())
x3 = x[2] if x[0] == x[1] else x[0] if x[1] == x[2] else x[1]
y3 = y[2] if y[0] == y[1] else y[0] if y[1] == y[2] else y[1]
print(x3, y3)