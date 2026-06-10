# Code to find sum of natural numbers upto n terms
# using recursion

def compute(n:int):
    if n == 1:
        return 1
    else:
        return (n + compute(n-1))
    
    
n = int(input('Enter number of terms: '))
sum = compute(n)
print(f'Sum of natural numbers upto {n} is {sum}')
