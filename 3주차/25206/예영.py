rate = 0 #학점*성적 변수
scoreSum = 0 #학점 변수

rating ={"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

for i in range(20):
    subject, score, grade = input().split()
    if grade == "P":
        continue #P는 건너뜀
    rate += float(score)*rating[grade] 
    scoreSum += float(score)

print(rate/scoreSum)
