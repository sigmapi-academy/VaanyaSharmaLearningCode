
start = 1
N = 20
print('Rowwise multiplication table: ')
while start <= N:
    t = 1
    print('Table of', start)
    while t < 10:
        p = start * t
        print(p,end=', ')
        t +=1
    print((start*t))
    start += 1