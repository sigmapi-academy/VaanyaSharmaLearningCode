try:
    numerator = int(input('Enter numerator: '))
    denominator = int(input('Enter denominator: '))
    quotient = numerator // denominator
    print("quotient =", quotient)
    print('Division performed successfully')
except ZeroDivisionError:
    print("Denominator as Zero...not allowed")
except ValueError:
    print('Only integers are allowed')
except:
    print('Other symbols are not allowed')

print("Outside try...except block")