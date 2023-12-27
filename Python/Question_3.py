# Write a program to display numbers from start to end range.

# Input Description:
# First line consists of input start & end range number

# Output Description:
# Output consists of total number of digits in a number.

# Sample Input :
# 4 7
# Sample Output :
# 4 5 6 7


# Get input values for start and end
start, end = map(int, input().split())

# Initialize an empty string to store the concatenated numbers
s = ''

# Iterate through the range from start to end (inclusive)
for i in range(start, end + 1):
    # Concatenate the current number (converted to string) with a space
    s = s + str(i) + " "

# Remove the last space using rstrip and print the result
print(s.rstrip())
