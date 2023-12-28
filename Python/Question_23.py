# Write a program to check whether a given number is even or odd. If even display “Even” else display “oDd”

# Input Description:
# First line consists of input number

# Output Description:
# Output consists of “Even” or “oDd”

# Sample Input :
# 2
# Sample Output :
# Even


# Function to check whether a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "oDd"

# Input the number
input_number = int(input())

# Check and display the result
result = check_even_odd(input_number)
print(result)
