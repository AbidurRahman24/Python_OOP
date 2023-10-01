# Read input string
input_string = input()

# Split the input string into words using space as the delimiter
words = input_string.split()

# Reverse each word, maintaining case, and store it in a list
reversed_words = [''.join(reversed(word)) for word in words]

# Join the reversed words to form the modified string
modified_string = ' '.join(reversed_words)

# Print the modified string
print(modified_string)
