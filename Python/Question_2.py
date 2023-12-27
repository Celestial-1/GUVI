# Write a program to find the area of a circle. If the input is zero and print the output “None” & If the output is float value round off upto 2 decimal places.

# Input Description:
# First line consists of input number

# Output Description:
# Output consists of Radius of a circle

# Sample Input :
# 5
# Sample Output :
# 78.54


# Get the radius input from the user
r = int(input())

# Calculate the area of the circle using the formula A = π * r^2
area = 3.1415926535 * (r ** 2)

# Round the calculated area to two decimal places
round_area = round(area, 2)

# Check if the radius is 0
if r == 0:
    # If the radius is 0, print "None"
    print("None")
else:
    # If the radius is not 0, print the rounded area of the circle
    print(round_area)
