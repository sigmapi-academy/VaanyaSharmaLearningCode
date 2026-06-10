# Write a recursive function to print a string backwards 

def printBackwards(st:str):
    if st != '':
        printBackwards(st[1:])
        print(st[0], end='')
    

s1 = input('Enter any word: ')
printBackwards(s1)
        
    