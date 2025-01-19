N = int(input())
list = list(map(int,input().split()))
list2 = list[:N]
a = int(input())
result=0
for i in range(N):
    if a==list[i]:
        result = result+1
print(result)
