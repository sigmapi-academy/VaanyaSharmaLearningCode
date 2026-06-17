def is_arm(n, order):
    if n == 0:
        return 0
    else:
        return ((n % 10) ** order) + is_arm(n // 10, order)

n = int(input('Enter any number: '))
order = len(n)
s = is_arm(n, order)
if s == n:
    print(n, 'is an armstrong number')
else:
    print(n, "isn't an Armstrong number")