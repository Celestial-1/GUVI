# Write a program to remove the empty string in the given input list.

# Input Description:
# First line contains size of the list Second line contains list of elements

# Output Description:
# Consist of string without empty string

# Sample Input :
# 3
# GUVI, ,Geek
# Sample Output :
# GUVI,Geek

# Using loops

# Function to remove empty strings from a list
def remove_empty_strings(elements):
    result = []
    for i in elements:
        if i != '':
            result.append(i)
    return result

# Input: Read the size and elements from the user
size = int(input())
elements = input().split(',')

# Output: Remove empty strings and print the result with commas
result = remove_empty_strings(elements)
for i in range(len(result)):
    print(result[i], end='')
    if i < len(result) - 1:
        print(',', end='')


# Using Join

def remove_empty_strings(size, elements):
    # Use list comprehension to filter out empty strings
    result = [element for element in elements if element != '']
    return result

# Input
size = int(input())
elements = input().split(',')

# Output
result = remove_empty_strings(size, elements)
print(','.join(result))
