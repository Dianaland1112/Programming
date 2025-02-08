while True:
    N = int(input())
    if N == -1:
        break
    else:
        result =[]
        for i in range(1,N):
            if N%i==0:
                result.append(i)
        if sum(result)==N:
            print(N,'=', end=' ')
            print(*result, sep=' + ')
        else :
            print(N,'is NOT perfect.')