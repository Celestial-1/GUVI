# Write a program to display only those numbers from a input list that satisfy the following conditions:

# The number must be divisible by 2
# If the number is greater than or equal 80, then skip it and move to the next number
# If the number is greater than 125, then stop the loop
# Input Description:
# First line contains size of the list Second line contains list of elements

# Output Description:
# Consists of only those numbers from a input list that satisfy the following conditions

# Sample Input :
# 6
# 6 4 1 80 24 125
# Sample Output :
# 6 4 24 125



def display_numbers(input_list):
    result = ""
    for number in input_list:
        # Check if the number is less than 80 and even
        if number < 80 and number % 2 == 0:
            result += str(number) + " "
        # Skip numbers between 80 and 125
        elif 80 <= number < 125:
            continue
        # Include numbers greater than or equal to 125 and break the loop
        elif number >= 125:
            result += str(number) + " "
            break

    # Display the result after removing trailing whitespace
    print(result.rstrip())

# Input handling
size = int(input())
elements = list(map(int, input().split()))

# Call the function with the provided elements
display_numbers(elements)
