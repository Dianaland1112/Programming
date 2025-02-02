# 1 6 12 18 24 
N = int(input())
if N!=1:
    i = 0
    result = 0
    while N>1:
        N = N - 6*i
        result +=1
        i+=1
    print(result)
else:
    print(1)