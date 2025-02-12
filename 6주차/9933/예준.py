n = int(input())
pw_candi = []

for i in range(n):
    pw = input()
    
    if (pw or pw[::-1]) in pw_candi or pw == pw[::-1]:
        pw_len = len(list(pw))
        mid_l = list(pw)[pw_len//2]
    else:
        pw_candi += [pw, pw[::-1]]

print(pw_len, mid_l)
