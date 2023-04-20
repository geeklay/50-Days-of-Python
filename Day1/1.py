from math import sqrt
def div_or_square(num):
    if num % 5 == 0: 
        return sqrt(num)
    return num % 5

def longest_value(x):
    l = 0 
    for i in x: 
        if len(str(x[i])) > l:
            l = len(str(x[i]))
            res = x[i] 
    return res             
    
print(div_or_square(int(input())))
print(longest_value(fruits))