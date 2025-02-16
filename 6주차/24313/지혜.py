a1, a0 = map(int, input().split()) #첫째 줄에 정수 a1, a0
c = int(input()) #다음 줄에 양의 정수 c
n0 = int(input()) #다음 줄에 양의 정수 n0

if c == a1 and a0 <= 0: #n>=n0여야 하니까 n대신 n0 ㄷ
	print(1)
elif c > a1 and n0*(c-a1) >= a0: #나눗셈 오차때문에 곱하기로 넘김
	print(1)
else:
	print(0)
