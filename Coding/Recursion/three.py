# power a, b using recursion

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)
    
#main code
print('Enter only positive numbers.')
a = float(input('Enter the base: '))
b = float(input('Enter raised to the power of: '))
result = power(a, b)
print(f'{a}, raised to the power of {b} is {result}')