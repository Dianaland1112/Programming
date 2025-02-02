table = []
for _ in range(9):
    row = list(map(int, input().split()))
    table.append(row)

max_value, max_r, max_c = -1, 0, 0

for i in range(9):
    for j in range(9):
        if max_value < table[i][j]:
            max_r = i+1
            max_c = j+1
            max_value = table[i][j]

print(max_value)
print(max_r, max_c)