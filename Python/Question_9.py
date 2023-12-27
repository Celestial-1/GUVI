# Write a program to check whether a given number is prime or not. If prime display “True” else “False”.

# Input Description:
# First line consists of input number

# Output Description:
# Output consists of prime or not

# Sample Input :
# 1
# Sample Output :
# False


def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input
num = int(input())

# Output
result = prime(num)
print(result)
