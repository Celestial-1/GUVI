# Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

# Input Description:
# First line of input consists of size of the list1 and list 2. Second & thrid line of input consist of elements of list1 and list2

# Output Description:
# Consist of list1 in original order and items from list2 in reverse order

# Sample Input :
# 2 2
# 1 2
# 3 4
# Sample Output :
# 1 4
# 2 3


# Function to iterate both lists simultaneously
def iterate_lists(list1, list2):
    # Iterate through the zipped combination of list1 and reversed list2
    for item1, item2 in zip(list1, reversed(list2)):
        # Print elements from list1 in original order and list2 in reverse order
        print(item1, item2)

# Input the size of the lists
size1, size2 = map(int, input().split())

# Input elements of list1 and list2
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# Call the function and print the result
iterate_lists(list1, list2)

