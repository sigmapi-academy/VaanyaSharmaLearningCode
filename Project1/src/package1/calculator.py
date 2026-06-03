import package2.arithmetic as arith

while True:
    op = input('Press x or X to exit or enter to continue: ')
    if op in ('x', 'X'):
        print('Good bye, \nThank you')
        exit()
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    op = input("+,-, *, //, %, ^ : ")
    
    match op:
        case '+':
            print(f'sum = {arith.add(x, y)}')
        case '-':
            print(f'difference = {arith.sub(x, y)}')
        case '*':
            print(f'product = {arith.multiply(x, y)}')
        case '//':
            print(f'Quotient = {arith.quotient(x, y)}')
        case '%':
            print(f'remainder = {arith.remainder(x, y)}')
        case '^':
            print(f'power = {arith.power(x, y)}')
        case _:
            print('Wrong option selected!')
            

