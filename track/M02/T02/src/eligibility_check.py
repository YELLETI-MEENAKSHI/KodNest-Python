student_marks=int(input("enter the marks:"))
student_attendance=int(input("enter the attendance:"))
project_completion=input("enter the status:")
if student_marks>=60:
    if student_attendance>=75:
        if project_completion=="yes":
            print("Eligible")
        else:
            print("Not Eligible")
    else:
      print("Not Eligible")
else:
    print("Not Eligible")