a = input()
list = []
result =[]
for i in range(len(a)):
    list.append(a[i])
for j in list:
    j_upper = j.upper()
    result.append(j_upper) # 대문자로 바꾸어 리스트화화
t=[]
for k in range(len(result)):
    t.append(result.count(result[k])) # 같은 문자가 몇개인지 확인ㄴ
l = t.index(max(t)) # 가장 많은 문자의 인덱스 확인
if max(t) == t.count(max(t)): # 가장 많은 문자가 하나일 때
    print(result[l]) 
else:
    print('?')

# 시간초과 ?