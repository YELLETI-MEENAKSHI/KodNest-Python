# Read how many numbers will be entered
number_count = int(input())

# Initialize the counters and total
total = 0
positive_count = 0
negative_count = 0
zero_count = 0

# Loop to read and analyze each number
for i in range(number_count):
    # Read the individual number
    current_number = int(input())
    
    # Add to total
    total = total + current_number
    
    # Check if positive, negative, or zero
    if current_number > 0:
        positive_count = positive_count + 1
    elif current_number < 0:
        negative_count = negative_count + 1
    else:
        zero_count = zero_count + 1

# Print the final results
print(f"Positive Count: {positive_count}")
print(f"Negative Count: {negative_count}")
print(f"Zero Count: {zero_count}")
print(f"Total: {total}")