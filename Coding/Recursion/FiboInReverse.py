
def printfibonacciSeqInReverse(n:int, a = 0, b = 1, i = 1):
    if i < n:
        printfibonacciSeqInReverse(n, b, a+b, i+1)
    print(a if i == 0 else b, end=' ')    

# main code
n = int(input('Enter number of terms: '))

printfibonacciSeqInReverse(n)

 