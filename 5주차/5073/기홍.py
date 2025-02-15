def is_valid(_list):
    if max(_list) >= (sum(_list) - max(_list)):
        return "Invalid"
    count = 0
    for i in range(2):
        for j in _list[i + 1 :]:
            if _list[i] == j:
                count += 1
    if count == 3:
        return "Equilateral"
    elif count == 1:
        return "Isosceles"
    else:
        return "Scalene"


while 1:
    _list = list(map(int, input().split()))
    if not (_list[1] and _list[0] and _list[2]):
        exit()
    print(is_valid(_list))
