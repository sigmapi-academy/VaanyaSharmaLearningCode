
def fibonacci(n:int):
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def numberOfterms(start:int, n:int):
    if start <= n:
        print(fibonacci(start))
        numberOfterms(start+1, n)
        

# main code
n = int(input('Enter number of terms: '))

numberOfterms(1, n)

 