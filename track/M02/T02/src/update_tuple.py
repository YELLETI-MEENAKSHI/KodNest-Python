# Read the course details
course_name = input("enter course name:")
current_week = input("enter current week:")
course_status = input("enter course status")

# Create the original tuple
course_details = (course_name, current_week, course_status)
print(course_details)

# Read the updated week
updated_week = input("enter updated week")

# Create and assign a new tuple
course_details = (course_name, updated_week, course_status)

# Display the updated tuple
print(course_details)