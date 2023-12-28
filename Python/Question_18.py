# Write a program to find words with both alphabets and numbers from an input string.

# Input Description:
# Consists of string

# Output Description:
# Consist of words with both alphabets and numbers

# Sample Input :
# GUVI Geek Network1
# Sample Output :
# Network1

def alphanumeric(input_string):
    words = input_string.split()
    output_words = []

    for word in words:
        if any(char.isdigit() for char in word) and any(char.isalpha() for char in word):
            output_words.append(word)

    return output_words

# Input
input_string = input()

# Output
output_words = alphanumeric(input_string)
print(" ".join(output_words))