student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# for student in student_attendance:
#     print(student)

print(list(student_attendance.items()))

# Destructure
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


attendance_values = student_attendance.values()
print(len(attendance_values))
