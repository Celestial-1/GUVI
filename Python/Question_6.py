# Write a program to print the first “n” Fibonacci series numbers, where n is a positive integer. If the input is zero and print the output “ZeRo”

# Input Description:
# First line consists of input number

# Output Description:
# Output consists of Fibonacci series

# Sample Input :
# 2
# Sample Output :
# 1 1


def fibonacci(n):
    # Initialize an empty list to store the Fibonacci series
    fib_series = []
    
    # Initialize the first two numbers in the Fibonacci series
    a, b = 1, 1

    # Iterate 'n' times to generate the Fibonacci series
    for i in range(n):
        # Append the current Fibonacci number to the list
        fib_series.append(a)

        # Update the values of 'a' and 'b' to generate the next Fibonacci number
        a, b = b, a + b

    # Return the generated Fibonacci series
    return fib_series

# Take user input for the number of Fibonacci numbers to generate
n = int(input())

# Check if the user input is 0
if n == 0:
    print("ZeRo")
else:
    # Call the fibonacci function with the user-input value
    result = fibonacci(n)

    # Print the generated Fibonacci series using unpacking (*result)
    print(*result)

