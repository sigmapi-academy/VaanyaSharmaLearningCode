# 6. Ask the user to enter two numbers and a choice of operation (+, -, *, /). Based on the 
# operation selected, perform the calculation and display the result. 
# Also, print whether the result is an integer or a float using isinstance(). 

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

oper = input("Select any operator (+ - * /): ")

res = 0
if oper == '+':
    res = num1 + num2
    print("sum =", res)
elif oper == '-':
    res = num1 - num2
    print("Diff:", res)
elif oper == '*':
    res = num1 * num2
    print("Product: ",res)
elif oper == '/':
    res = num1 / num2
    print("Quotient:", res)

if isinstance(res,float):
    print('Result is in float')
elif isinstance(res,int):
    print('Result is in int')
else:
    print('Error')
