N,b = map(str,input().split())
B = int(b)
number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0
for i, num in enumerate(N[::-1]):
    result += B**i*number.index(num)

print(result)