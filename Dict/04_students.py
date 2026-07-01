students_info = {}
line = input()

while ":" in line:
    name, student_id, course = line.split(":")
    if course not in students_info:
        students_info[course] = {}

    students_info[course][student_id] = name
    line = input()
    course = " ".join(line.split("_"))

    for key, value in students_info.items():
        if key == course:
            for student_id, name in value.items():
                print(f"{name} - {student_id}")