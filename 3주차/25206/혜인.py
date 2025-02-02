grade_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
#grade = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
#score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total = 0  # 학점 * 과목평점의 합
total_time = 0  # 총 학점
for _ in range(20):
    subject, time, grade = input().split()
    time = float(time)
    if grade != "P":
        total += time * grade_dict[grade]
        total_time += time 

print(f"{total / total_time:.6f}")   

