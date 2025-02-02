N=int(input())
list=[]
for i in range(N):
    list.append(input())
result=N
for i in range(N):
    if(len(list[i])>2):
        temp=0
        for j in range(len(list[i])):
            for x in range(j, len(list[i])):
                if(list[i][j]==list[i][x]):
                    if(abs(x-j)>1 and list[i][j]!=list[i][x-1]):
                        temp+=1
        if(temp>0):
            result-=1
    else:
        pass
print(result)