# 전체 학생 번호 (1부터 30까지)
all_students = list(range(1, 31))

# 과제를 제출한 학생 번호 입력받기
submitted_students = []
for _ in range(28):
    submitted_students.append(int(input()))

# 과제를 제출하지 않은 학생 번호 구하기
missing_students = []
for student in all_students:
    if student not in submitted_students:
        missing_students.append(student)

# 결과 출력 (작은 번호부터 출력)
missing_students.sort()
print(missing_students[0])  # 가장 작은 번호
print(missing_students[1])  # 다음 번호
