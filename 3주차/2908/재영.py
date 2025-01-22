a,b = map(str,input().split())
A =[]
B=[]
for i in list(a):
    A.append(i)
for j in list(b):
    B.append(j)
A.reverse()
B.reverse()              ###동생이 읽은 두 수수
a=''
b=''
for i in list(A):
    a+=i
for j in list(B):
    b+=j
if int(a)>int(b):
    print(int(a))
else:
    print(int(b))     ### 동생이 읽은 두 수 크기 비교