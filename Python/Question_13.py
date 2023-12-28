# Write a program to print the given input string into 3 times in a single line.

# Input Description:
# First line consists of input string

# Output Description:
# Consist of string into 3 times in a single line

# Sample Input :
# GuVI
# Sample Output :
# GuVI GuVI GuVI


# Get input string
input_string = input()

# Print the string three times in a single line
print(input_string, input_string, input_string)

# Using *

# Get input string
input_string = input()

# Replicate the string three times with a space separator
result = ((input_string + " ") * 3)
print(result.rstrip())

# Using Join

# Get input string
input_string = input()

# Print the string three times
output_string = ' '.join([input_string] * 3)
print(output_string)
