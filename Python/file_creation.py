import os
for i in range(4,25) :
    old_name=(f'GUVI\Python\Question_{i+1}')
    new_name=(f'GUVI\Python\Question_{i+1}.py')
    os.rename(old_name,new_name)
    # open(f'GUVI\Python\Question_{i+1}', 'w')