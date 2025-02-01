N = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(N):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            if i>=100 or j>=100:
                break
            else:
                paper[i][j]=1
                
result = 0
for i in range(100):
    result+=paper[i].count(1)

print(result)