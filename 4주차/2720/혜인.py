q, d, n, p = 0, 0, 0, 0

test_case = int(input())

for _ in range(test_case):
    money = int(input())
    q = money // 25
    money %= 25

    d = money // 10
    money %= 10

    n = money // 5
    money %= 5

    p = money
    print(q, d, n, p) 
    
