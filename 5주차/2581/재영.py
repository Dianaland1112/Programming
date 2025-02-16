''''''''''''''''
M = int(input())
N = int(input())
result=[]
for i in range(M,N+1):
    a =[]
    for j in range(1,i):
        if i%j==0:
            a.append(j)
    if len(a)==1:
            result.append(i)
if len(result)!=0:
    print(sum(result))
    print(min(result))
else:
    print('-1')
'''''''''

M = int(input())
N = int(input())

def is_prime(n):
    if n < 2:
        return False  # 1은 소수가 아님
    for i in range(2, int(n ** 0.5) + 1):  # √n까지만 검사
        if n % i == 0:
            return False
    return True

primes = [i for i in range(M, N + 1) if is_prime(i)]  # 소수만 리스트에 저장

if primes:
    print(sum(primes))  # 소수 합 출력
    print(min(primes))  # 가장 작은 소수 출력
else:
    print('-1')