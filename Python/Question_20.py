# Write a program to calculate the sum of series up to n term. For example, if n=2 the series will become 2 + 22 = 24

# Input Description:
# First line consists of input number

# Output Description:
# Output consists of sum of series.

# Sample Input :
# 2
# Sample Output :
# 24


# Function to calculate the sum of series
def series_sum(n):
    term = ""
    series_sum = 0
    for i in range(1, n + 1):
        term += str(2)
        series_sum += int(term)
    return series_sum

# Input the number of terms
n = int(input())

# Call the function and print the result
result = series_sum(n)
print(result)


# If you want output for n=4 : 4+44+444+4444 then

# Function to calculate the sum of series
def series_sum(n):
    term = ""
    series_sum = 0
    for i in range(1, n + 1):
        term += str(n)
        series_sum += int(term)
    return series_sum

# Input the number of terms
n = int(input())

# Call the function and print the result
result = series_sum(n)
print(result)
