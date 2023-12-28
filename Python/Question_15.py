# Write a program to print the value from the given index range from the string. If the step count is zero print the output to “Zero”

# Input Description:
# First line consists of string Second line consist of start, end & step value

# Output Description:
# Output consist of string

# Sample Input :
# GUVI Geek Network Private Limited
# -1 -12 -2
# Sample Output :
# dtmLea

def substring(input_string, start, end, step):
    if step == 0:
        print("Zero")
        return

    result = input_string[start:end:step]
    print(result)

# Read input
input_string = input().strip()
start, end, step = map(int, input().strip().split())

# Call the function
substring(input_string, start, end, step)

