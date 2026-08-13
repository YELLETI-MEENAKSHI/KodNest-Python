# Read the number of students
student_count = int(input("Enter the student count:"))
total_marks = 0
passed_count = 0
failed_count = 0

for i in range(student_count):
    marks = int(input("enter the marks:"))
    total_marks = total_marks + marks
    
    if marks >= 40:
        passed_count = passed_count + 1
    else:
        failed_count = failed_count + 1

print(f"Total Marks: {total_marks}")
print(f"Passed Students: {passed_count}")  # Fixed 'ppint' to 'print'
print(f"Failed Students: {failed_count}")

if failed_count == 0:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Needs Improvement")