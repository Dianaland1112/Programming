# 아직 미 해결, 이어서 풀 예정
grades = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
    "P": 0.0
}

total = 0
cnt = 0

for i in range(20):
    subject, score, grade = map(str, input().split())
    if grade=='P': 
        continue
    cnt += 1 
    score = float(score) * 10000 + (grades[grade]*10000)
    total += score

result = total/(cnt *10000)
print(result)
