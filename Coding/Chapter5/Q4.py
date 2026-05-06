
def sumOfNums(liOfNums: list):
    sum = 0
    for n in liOfNums:
        sum += n
    return sum

# main code
li = eval(input('Enter the list of numbers: '))

S = sumOfNums(li)

print("Sum = ",S, sep ='')

print(sum(li))