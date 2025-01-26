grade_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 
              'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
major_sum = 0
total_credit = 0

for _ in range(20):
    subject, credit, grade = input().split()
    if grade != 'P':
        major_sum += float(credit) * grade_dict[grade]
        total_credit += float(credit)

major_grade = major_sum / total_credit
print(round((major_grade), 6))