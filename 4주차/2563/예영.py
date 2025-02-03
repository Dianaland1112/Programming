number=int(input())

size=[[0]*100 for _ in range(100)]
for _ in range(number):
    y1, x1=map(int, input().split())

    for i in range(x1, x1+10):
        for j in range(y1, y1+10):
            size[i][j]=1

result=0
for k in range(100):
    result += size[k].count(1)

print(result)
