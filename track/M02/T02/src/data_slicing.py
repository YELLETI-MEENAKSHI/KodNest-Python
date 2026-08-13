word = input("enter word")

first = int(input("enter first:"))
second = int(input("enter second"))
third = int(input("enter third"))

numbers = [first, second, third]
record = (first, second, third)

# Slice the string, list and tuple
sliced_string = word[1:-1]
sliced_list = numbers[:2]
reversed_tuple = record[::-1]

print(f"Middle: {sliced_string}")
print(f"First Two: {sliced_list}")
print(f"Reversed Tuple: {reversed_tuple}")