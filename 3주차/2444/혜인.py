a = int(input())
for i in range(1,a+1):
    print(" "*(a-i)+"*"*(2*i-1))
for i in range(a-1,0, -1):
    print(" "*(a-i)+"*"*(2*i-1))#, 대신 + 사용하기. 
# , 사용시 빈칸 생김
