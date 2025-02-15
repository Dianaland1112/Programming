n, b = input().split()
digit = len(n)
b = int(b)
res = 0
# b 진수를 10진수로 변환하기 위한 방법은 몇 번째 자리인지 파악하고 제곱해서 더하는 것.
for i in range(digit):
    check = n[i]
    if "A" <= check <= "Z":
        res += int((ord(check) - 55)) * (b ** (digit - i - 1))
    else:
        res += int(check) * (b ** (digit - i - 1))
print(res)
