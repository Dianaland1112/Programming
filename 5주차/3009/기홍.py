_list = []
for _ in range(3):
    _list.append(list(map(int, input().split())))

x_result = []
y_result = []
for a, b in _list:
    if a in x_result:
        x_result.remove(a)
    else:
        x_result.append(a)
    if b in y_result:
        y_result.remove(b)
    else:
        y_result.append(b)
print(f"{x_result[0]} {y_result[0]}")
