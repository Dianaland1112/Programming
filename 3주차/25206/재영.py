"""
N = []
S = []
result=0
for i in range(20):
    a,b,c = input().split(' ')
    if c==


for i in range(len(N)):
    result = result + N[i]*S[i]
print(result/len(N))
"""
rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]         #if문 사용 너무 불편, index로 매치 시키기기

result=0
N=0
for i in range(20):
    a,b,c=input().split()
    if c!='P':
        result+=float(b)*(grade[rating.index(c)]) 
        N +=float(b)
    else:
        continue
print(result/N)

