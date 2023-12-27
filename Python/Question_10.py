# Write a program to check whether a number is divisible by 11 or not. If divisible display “yes” else display “no”

# Input Description:
# First line consists of input number

# Output Description:
# Output consists of “yes” or “no”

# Sample Input :
# 22
# Sample Output :
# yes



# Input
num = int(input())

# Check if the number is divisible by 11
if num % 11 == 0:
    result = "yes"
else:
    result = "no"

# Output
print(result)
