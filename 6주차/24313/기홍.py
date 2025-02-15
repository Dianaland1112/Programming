a, b = map(int,input().split())

c = int(input())
n = int(input())

# g = 1 if a else 0 // g(x)의 빅오는 f(x)이고 만약 f(x)=ax+b 라고 하면 a 영향을 받아서
# g(x)의 값이 달려져야 하는 것이 아닌지..? 근데 왜 틀릴까요.?

# 2차 함수를 대입하여 0 <= (cg-a)n -b 형식으로 생각하여 문제를 푼다. 
def o_natfun():
    if (c-a) < 0:
        return 0
    elif (c-a) >= 0 and 0 <= (c-a)*n-b:
        return 1

print(1 if o_natfun() else 0)
