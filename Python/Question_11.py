# Write a program to print the reverse order in the given input list

# Input Description:
# First line contains size of the list Second line contains list of elements

# Output Description:
# Consist of list if numbers in the reverse order

# Sample Input :
# 5
# 78 66 89 65 64
# Sample Output :
# 64 65 89 66 78

# for loop method & strip

# Get the size of the list from the user
size = int(input())

# Get the list of elements from the user
elements = list(map(int, input().split()))

# Reverse the list
elements.reverse()

# Initialize an empty string to store the reversed elements with space separator
s = ""

# Iterate through the reversed list and build the string
for i in elements:
    s += str(i) + " "  # Convert each element to a string and append with a space

# Print the final string, removing the trailing space
print(s.strip())



# .join concatination method 

# Input
size = int(input())
numbers = list(map(int, input().split()))

# Reverse the list
reverse_order = numbers[::-1]

# Output
print(" ".join(map(str, reverse_order)))
