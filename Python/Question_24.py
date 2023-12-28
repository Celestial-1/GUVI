# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Input Description:
# First line of input consists of size of the list1 and list 2. Second & thrid line of input consist of elements of list1 and list2

# Output Description:
# Consist of string

# Sample Input :
# 2 2
# G V
# U I
# Sample Output :
# GU VI


def add_lists(list1, list2):
    result = []
    for item1, item2 in zip(list1, list2):
        result.append(item1 + item2)

    # Add any leftover items
    if len(list1) > len(list2):
        result.extend(list1[len(list2):])
    elif len(list2) > len(list1):
        result.extend(list2[len(list1):])

    return result

# Input
size1, size2 = map(int, input().split())
list1 = input().split()
list2 = input().split()

# Output
result_list = add_lists(list1, list2)
print(" ".join(result_list))
