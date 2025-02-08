# 입력받기
T = int(input())  # 테스트 케이스의 수 입력
results = []  # 각 테스트 케이스의 동전 개수를 문자열로 만들어 저장

# 각 테스트 케이스에 대해 동전 개수 계산
for i in range(T):
    C = int(input())  # 거스름돈 입력 (센트 단위)
    
    # 동전 단위 (센트)
    quarters = C // 25  # 쿼터의 개수
    C %= 25  # 나머지 거스름돈
    
    dimes = C // 10  # 다임의 개수
    C %= 10  # 나머지 거스름돈
    
    nickels = C // 5  # 니켈의 개수
    C %= 5  # 나머지 거스름돈
    
    pennies = C  # 남은 페니의 개수
    
    # 숫자 -> 문자열로 결과 저장 (문제 : 각 동전 개수를 공백으로 구분해서 출력)
    results.append(str(quarters) + " " + str(dimes) + " " + str(nickels) + " " + str(pennies))


# 결과 출력
for result in results:
    print(result)
