# Using append() and insert()
# Write a program that takes a list of colors. Add a new color to the end of the list using append(),
# and insert another color at the second position using insert().

colours=[]

while True:
    clr = input('Enter colour name: ')
    colours.append(clr)
    done = input('Type done to stop appending: ')
    if done.lower() == 'done':
        break
print(colours)
clr = input('Enter colour name: ')
colours.insert(1, clr)
print(colours)


    