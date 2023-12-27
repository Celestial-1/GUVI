# Write a program to find the largest of three numbers.

# Input Description:
# First line consists of input number

# Output Description:
# Output consists of largest of three numbers

# Sample Input :
# 5 8 7
# Sample Output :
# 8

# Get user input for three integers separated by spaces
input_str = input()

# Split the input string into a list of strings
input_list = input_str.split()

# Map each element in the list to an integer
a, b, c = map(int, input_list)

# Find the greatest among a, b, and c
greatest = max(a, b, c)

# Print the greatest integer
print(greatest)
