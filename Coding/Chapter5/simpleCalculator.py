def add(a:float, b:float):
    return a+b

def subtract(a:float, b:float):
    return a-b

def product(a:float, b:float):
    return a*b

def division(a:float, b:float):
    return a/b

def quotient(a:float, b:float):
    return a//b

def remainder(a:float, b:float):
    return (a%b)

def power(a:float, b:float):
    return (a**b)

#main code
print('='*50)
print('Welcome to Simple calculator')
print('='*50)
while True:
    print('Press +, -, *, /, //, %, **, x(exit): ')
    op = input()
    match op:
        case '+':
            n1 = float(input('Enter first number: '))
            n2 = float(input('Enter second number: '))
            res = add(n1, n2)
            print(f'Result: {res}')
        case '-':
            n1 = float(input('Enter first number: '))
            n2 = float(input('Enter second number: '))
            res = subtract(n1, n2)
            print(f'Result: {res}')
        case '*':
            n1 = float(input('Enter first number: '))
            n2 = float(input('Enter second number: '))
            res = product(n1, n2)
            print(f'Result: {res}')
        case '/':
            n1 = float(input('Enter first number: '))
            n2 = float(input('Enter second number: '))
            res = division(n1, n2)
            print(f'Result: {res}')
        case '//':
            n1 = float(input('Enter first number: '))
            n2 = float(input('Enter second number: '))
            res = quotient(n1, n2)
            print(f'Result: {res}')
        case '%':
            n1 = float(input('Enter first number: '))
            n2 = float(input('Enter second number: '))
            res = remainder(n1, n2)
            print(f'Result: {res}')
        case '**':
            n1 = float(input('Enter first number: '))
            n2 = float(input('Enter second number: '))
            res = power(n1, n2)
            print(f'Result: {res}')
        case 'x':
            print('Good Bye')
            exit(0) #terminate the infinite loop.
        case _:
            print('Wrong option selected')
