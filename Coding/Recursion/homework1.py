# def sumOfSeries(terms):
#     if terms > 1:
#         print(terms**2, ' + ', end='')
#         return terms**2 + sumOfSeries(terms-1)
        
#     else:
#         print(terms**2, ' = ', end = '')
#         return terms**2
        

def sumOfSeries(terms, start = 1):
    if start < terms:
        print(start**2, ' + ', end='')
        return start**2 + sumOfSeries(terms, start+1)
    else:
        print(start**2, ' = ', end = '')
        return start**2
        
#main code
N = int(input('Enter number of terms: '))
sum = sumOfSeries(N)
print(sum)