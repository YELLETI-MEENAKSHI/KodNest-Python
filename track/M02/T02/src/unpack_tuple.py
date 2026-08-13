name = input("enter name")
course = input("enter course:")
score = int(input("enter score:"))

# Create the tuple
student_record = (name, course, score)

# Unpack the tuple
name = student_record[0]
course = student_record[1]
score = student_record[2]

# Display the unpacked values
print(f"Name: {name}")      # Fixed: removed the extra single quote
print(f"Course: {course}")
print(f"Score: {score}")    # Fixed: changed 'print' to 'print'