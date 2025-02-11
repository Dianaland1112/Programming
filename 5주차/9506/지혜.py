while True:
    n = int(input())  # 숫자 입력 받기

    if n == -1:  # 입력의 마지막엔 -1이 주어진다 -> -1이 입력되면 종
        break

    div_sum = 0  # 약수들의 합
    div_str = ""  # 약수들을 저장할 문자열

    
    for i in range(1, n): # 1부터 n-1까지 모든 숫자를 검사 -> 약수들은 오름차순으로 나열된다.
        if n % i == 0:  # i가 n의 약수라면
            div_sum += i  # 약수들의 합에 더하기

            if div_str: # 첫번째 약수가 아닐때부터 + 추가 
                div_str += " + "
            div_str += str(i)  # 문자열에 약수 추가
            
    if div_sum == n: 
        print(f"{n} = {div_str}") # 약수들의 합이 n과 같으면 n이 완전수
    else:
        print(f"{n} is NOT perfect.") # n이 완전수가 아니라면 n is NOT perfect. 를 출력
