hang=[]
yul=[]

for i in range(9):
    a=list(map(int,input().split()))
    hmax=max(a)
    ymax=a.index(hmax)+1
    hang.append(hmax)
    yul.append(ymax)

print(max(hang))
print(hang.index(max(hang))+1,yul[hang.index(max(hang))])
