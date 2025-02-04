X = int(input())
group = 1

while group < X:
    X -= group
    group += 1
    
if group % 2 == 0:
    a = X
    b = group - X + 1
else:
    a = group - X + 1
    b = X

print(str(a)+'/'+str(b))