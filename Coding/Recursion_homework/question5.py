def sum_of_squares(n):
    if n == 0:
        return 0
    else:
        digit = n % 10
        return (digit ** 2) + sum_of_squares(n // 10)

def is_lucky(n):
    if n ==1:
        return True
    elif n==4:
        return False
    else:
        return is_lucky(sum_of_squares(n))

n = int(input('Enter any number: '))
if is_lucky(abs(n))==True:
    print(n,'is a lucky number')
else:
    print(n, 'is not lucky number')