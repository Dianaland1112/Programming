x_list = []
y_list = []
a = int(input())
for _ in range(a):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)
print((max(x_list) - min(x_list)) * (max(y_list) - min(y_list)))
