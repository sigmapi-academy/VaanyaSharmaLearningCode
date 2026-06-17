def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

n = int(input('Enter any number: '))
s = sum_of_digits(n)
print(f'Sum of digits of {n} = {s}')