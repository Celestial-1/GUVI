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



# Input
size = int(input())
numbers = list(map(int, input().split()))

# Reverse the list
reverse_order = numbers[::-1]

# Output
print(" ".join(map(str, reverse_order)))
