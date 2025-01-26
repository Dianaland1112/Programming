N = int(input())
result=list()

for i in range(N):
    Str=""
    R, S=input().split()

    for j in S:
        Str += j*int(R)

    result.append(Str)

for i in result:
    print(i)
