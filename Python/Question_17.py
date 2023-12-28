# Write a program to remove all characters from a string except integers

# Input Description:
# Consist of string and integers

# Output Description:
# Consist of integers present in the given string.

# Sample Input :
# GUVI 2 3 Geek
# Sample Output :
# 23

# Get input from the user
s = input()

# Remove leading and trailing whitespaces
s = s.strip()

# Initialize an empty string to store the result (digits)
r = ""

# Iterate through each character in the input string
for i in s:
    # Check if the character is a digit
    if i.isdigit():
        # Append the digit to the result string
        r += i

# Print the final result containing only digits
print(r)



# Using join

def extract_integers(input_string):
    result = ''.join(char for char in input_string if char.isdigit())
    return result

# Input
input_string = input()

# Output
output_result = extract_integers(input_string)
print( output_result)


