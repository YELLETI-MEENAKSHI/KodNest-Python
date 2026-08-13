n = int(input("enter n"))
numbers = []

# Read n integers and add them to the list
for i in range(n):
    num = int(input("Enter num:"))  # Fixed: changed 'n' to 'num'
    numbers.append(num)

print(numbers)