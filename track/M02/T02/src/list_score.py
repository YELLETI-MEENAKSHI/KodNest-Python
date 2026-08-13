n = int(input("enter n"))
scores = []

# Read and store all scores
for i in range(n):
    score = int(input("enter the score:"))
    scores.append(score)

search_score = int(input("enter search score"))
highest_score = max(scores)
lowest_score = min(scores)
total_score = sum(scores)

# Display the highest, lowest and total scores
print(f"Highest Score: {highest_score}")  # Fixed: moved " outside the }
print(f"Lowest Score: {lowest_score}")
print(f"Total Score: {total_score}")

# Display whether search_score is present
if search_score in scores:
    print("Search Result: Found")
else:
    print("Search Result: Not Found")