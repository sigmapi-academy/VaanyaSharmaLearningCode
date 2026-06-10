# Find factorial of a number using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
#main code
n = int(input('Enter any number: '))
f = factorial(n)
print(f'{n}! = {f}')