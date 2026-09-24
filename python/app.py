student_name = input("Enter your name")
subject1 = int(input("Enter first subject marks"))
subject2 = int(input("Enter second subject marks"))
subject3 = int(input("Enter third subject marks"))
subject4 = int(input("Enter fourth subject marks"))
subject5 = int(input("Enter fifth subject marks"))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
average_marks = total_marks / 5

if average_marks >= 80:
    grade = "A"
elif average_marks >= 65:
    grade = "B"
elif average_marks >= 50:
    grade = "C"
    grade = "F"

if average_marks >= 40:
    status = "PASS"
    print("PASS.")
else:
    status = "FAIL"
    print("FAIL.")

print("student:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("subject1:", subject1)
print("subject2:", subject2)
print("subject3:", subject3)
print("subject4:", subject4)
print("subject5:", subject5)
print("Grade:", grade)
print("status:", status)
