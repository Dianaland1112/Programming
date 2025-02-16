while(1):
    a, b, c = map(int, input().split())
    tri = [a ,b ,c]
    tri.sort()
    
    if a == b == c:
        if a == 0:
            break
        else:
            print("Equilateral")
    elif tri[2] < tri[0] + tri[1]:
        if tri[0] == tri[1] or tri[1] == tri[2]:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')
