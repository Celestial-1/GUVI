# Write a program to count the total number of digits in a number.

# Input Description:
# First line consists of input number

# Output Description:
# Output consists of total number of digits in a number.

# Sample Input :
# 345
# Sample Output :
# 3


# Input the number
number = int(input())

# Convert the number to a string and calculate the length
num_str = str(number)
num_digits = len(num_str)

# Output the total number of digits
print(num_digits)
