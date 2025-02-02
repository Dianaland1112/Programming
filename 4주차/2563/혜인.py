def checkarea(x1, y1, x2, y2):
    n = 0
    if abs(x1 - x2) < 10 or abs(y1 - y2) < 10:
        area = (abs(x1 - x2)) * (abs(y1 - y2))
        n += 1
    print(area)

listx = {(x1 + 10), (x2 + 10), (x3 + 10), (x1 + 10)}
listy = {(y1 + 10), (y2 + 10), (y3 + 10), (y1 + 10)}
area_total = 0
for i in range :
    checkarea(listx[i], listy[i], listx[i+1], listy[i+1])
    area_total += area
    if n == 3:
        (max(listx[i]) - median(listx[i])) * (max(listx[y) - median(listx[i]))