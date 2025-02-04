N, B = input().split()
B = int(B)
result = 0

for i in range(len(N)):
    if N[i].isdigit():
        result += int(N[i]) * (B ** (len(N)-i-1))
    else:
        result += (ord(N[i])-ord('A')+10) * (B ** (len(N)-i-1))
    
print(result)