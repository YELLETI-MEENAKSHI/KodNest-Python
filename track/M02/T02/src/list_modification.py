original_scores = []

for _ in range(3):
    original_scores.append(int(input()))

alias_scores = original_scores

# Modify the shared list through alias_scores
replacement_score = int(input())
additional_score = int(input())

alias_scores[0] = replacement_score
alias_scores.append(additional_score)

# Display both variables and check whether they share one object
shared_obj = original_scores is alias_scores

print(f"Original: {original_scores}")
print(f"Alias: {alias_scores}")
print(f"Shared Object: {shared_obj}")