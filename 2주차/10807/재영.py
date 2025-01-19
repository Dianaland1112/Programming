a = input()
result=[]
k=1
for i in range(len(a)):
    result.append(a[i])
result.sort()
result.reverse()
for i in range(len(a)):
    print(int(result[i]),end='')