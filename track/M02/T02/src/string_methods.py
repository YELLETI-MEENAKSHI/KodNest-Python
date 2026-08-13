sentence = input("enter sentence:")

# Clean and normalize the sentence
sentence = sentence.strip()
print("Cleaned:", sentence)

sentence = sentence.lower()
sentence = sentence.replace(".", "")
print("Normalized:", sentence)

# Split the sentence and create the slug
words_list = sentence.split()
print("Words:", words_list)

word = "-".join(words_list)
print("Slug:", word)

# Produce the uppercase form and search result
sentence = " ".join(words_list)
sentence = sentence.upper()
print("Uppercase:", sentence)

position = sentence.find("PYTHON")
print("Python Position:", position)