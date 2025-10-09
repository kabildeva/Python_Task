total_classes = int(input("Enter total classes: "))
class_attended = int(input("Enter classes attended: "))

attendance = (class_attended / total_classes) * 100
print("Attendance:", attendance, "%")

if attendance >= 75:
    print("Allowed for exam")
else:
    print("Not allowed for exam")
