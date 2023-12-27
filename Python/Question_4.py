# Write a program to convert Celsius to Fahrenheit. If the output is float value round off upto 1 decimal places.

# Input Description:
# First line consists of input number celsius

# Output Description:
# Output consists of Fahrenheit

# Sample Input :
# 78
# Sample Output :
# 172.4


# Input Celsius temperature
celsius = float(input())

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Round off to 1 decimal place if the result is a float
if isinstance(fahrenheit, float):
    fahrenheit = round(fahrenheit, 1)

# Output Fahrenheit temperature
print(fahrenheit)