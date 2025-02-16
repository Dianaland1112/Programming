def result(a, b):
    if (a % b) == 0:
        return 1  # is multiple
    elif (b % a) == 0:
        return 2  # is factor
    else:
        return 0


while 1:
    a, b = map(int, input().split())
    if not a and not b:
        break
    r = result(a, b)
    if not r:
        print("neither")
    else:
        print("factor" if r == 2 else "multiple")
