# multiplication table from 1 to 20

start = 1
N = 20

while start <= N:
    t = 1
    print('Table of', start)
    while t <= 10:
        p = start * t
        print(start,'*',t,'=',p)
        t +=1
    print()
    start += 1
    
    
    