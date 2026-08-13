def add_student(name, students=[]):
    students.append(name)
    print(students)
    # Write your code here
    pass

first_name = input("enter first name:")
second_name = input("enter second name:")
third_name = input("enter third name:")

add_student(first_name)
add_student(second_name)
add_student(third_name)