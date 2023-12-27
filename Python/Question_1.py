# Write a program to calculate the area and volume of the Cube.

# Input Description:
# First line consists of input number

# Output Description:
# 1. First line indicates area of the cube 2. Second line indicates colume of the cube

# Sample Input :
# 9
# Sample Output :
# 486
# 729


#Taking input
#print("Enter Side Of Cube :")
side=int(input())

#Surface Area of Cube 
area = 6*(side**2)
print(area)

#Volume of Cube
vol = side**3
print(vol)