# Write a program to count all the characters in the given string

# Input Description:
# Consist of string

# Output Description:
# Output consists of count all the characters in the given string

# Sample Input :
# GUVI
# Sample Output :
# 4



# Function to calculate the length of a string excluding spaces
def result(s):
    # Replace spaces with an empty string and return the length
    return len(s.replace(" ", ""))

# Input the string
input_string = input()

# Print the result (length of the string excluding spaces)
print(result(input_string))
