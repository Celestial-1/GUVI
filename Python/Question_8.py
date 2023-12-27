# Write a program to find the area of a rectangle. If the input or output value is floating point roundoff to nearest integer.

# Input Description:
# First line consists of input number

# Output Description:
# Output consists of area of rectangle

# Sample Input :
# 2 4
# Sample Output :
# 8

def calculate_rectangle_area(length, width):
    area = length * width
    return round(area)

# Input
input_values = input().split()
length = float(input_values[0])
width = float(input_values[1])

# Calculate and round off the area
area = calculate_rectangle_area(length, width)

# Output
print(area)
