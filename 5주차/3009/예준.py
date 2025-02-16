lix = []
liy = []
for i in range(3):
    x,y = map(int, input().split())
    lix.append(x)
    liy.append(y)

if lix.count(lix[0]) == 2:
    lix = [i for i in lix if i != lix[0]]
if liy.count(liy[0]) == 2:
    liy = [i for i in liy if i != liy[0]]
x = lix[0]
y = liy[0]

print(x,y)
