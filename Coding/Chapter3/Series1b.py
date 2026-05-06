# 1. Write separate programs in Python to display the first N terms of the following  series: 
# Output: 1, 2, 4, 7, 11, …

# 1, 1+1=2, 2+2=4, 4+3=7, 7+4=11, ... so on

n = int(input('Enter number of terms: '))

start = 0
t = 1
while start < n - 1: #n=5
    t += start      # 1, 2, 4, 7, 11
    print(t,', ',sep='',end='') #1, 2, 4, 7, 
    start += 1      # 1, 2, 3, 4, 5
t += start # 11
print(t) #1, 2, 4, 7, 11
