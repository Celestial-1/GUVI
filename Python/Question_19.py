# Write a program to print the index value from the given string.If the given index is not available print “None”.

# Input Description:
# First line consists of string Second line consist of index value

# Output Description:
# Output consists of index value from the given string

# Sample Input :
# GUVI
# 2
# Sample Output :
# U


# Function to get character at index or print "None" if index is out of bounds
def get_char_at_index(input_str, index):
    if 1 <= index < len(input_str):
        return input_str[index-1].capitalize()
    else:
        return "None"

# Input
input1 = input()
input2 = input()

# Output
if (input1.isdigit()):
    print(get_char_at_index(input2,int(input1)))
elif (input2.isdigit()):
    print(get_char_at_index(input1,int(input2)))
else:
    print("None")
