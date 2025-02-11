M = int(input())  # 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
N = int(input())

primes = []  # 소수를 저장할 리스트

for num in range(M, N + 1): # M부터 N까지 검사

    num_is_prime = True  # 소수라고 가정
    for i in range(2, num): # 2부터 num-1까지의 수를 나눈다.
        if num % i == 0:  # 나누어 떨어지면 소수가 아니다
            num_is_prime = False # 소수가 아니면 반복문 종료
            break  

    if num_is_prime:  # 소수라면 리스트에 추가
        primes.append(num)

if primes:
    print(sum(primes))  # 소수들의 합
    print(min(primes))  # 소수 중 최솟값
else:
    print(-1)  # 소수가 없으면 -1 출력
    
#틀렸습니다라고 뜹니다. 
