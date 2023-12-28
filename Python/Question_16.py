# Write a program to calculate the sum of all numbers from 1 to a given number. If the input is zero print “0”

# Input Description:
# First line consists of input number

# Output Description:
# Output consists sum of all numbers

# Sample Input :
# 2
# Sample Output :
# 3


# Using for loop

# Get input from the user
num = int(input())

# Initialize sum variable
sum = 0

# Check if the input number is zero
if num == 0:
    sum = 0
else:
    # Iterate from 1 to the input number (inclusive) and add each number to the sum
    for i in range(1, num + 1):
        sum += i

# Print the final sum
print(sum)

# Using formula (n * (n + 1)) // 2

def calculate_sum(n):
    if n == 0:
        print("0")
        return

    # Using the formula for the sum of the first n natural numbers: sum = n * (n + 1) / 2
    result = (n * (n + 1)) // 2
    print(result)

# Read input
n = int(input().strip())

# Call the function
calculate_sum(n)
