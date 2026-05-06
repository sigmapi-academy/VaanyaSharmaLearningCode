print('Handling exception using try... except... else')

try:
    numerator = int(input(" Enter numerator: "))
    denominator = int(input(' Enter denominator: '))
    quotient = numerator / denominator
    print(' Division performed successfully')
except ZeroDivisionError:
    print(' Denominator as zero is not allowed')
# except ValueError:
#     print(' Only integers should be entered')

else:
    print(' The result of division operation is:', quotient)

finally:
    print('This is the end of the code.')
    
    