fb = open("FileHandling/DataFiles/flowers.txt", "r")

print("Press enter key to continue and x or X to exit...")
while True:
    line = fb.readline()
    if not line:
        print('End of poetry')
        break
    print(line, end='')
    x = input()
    if x in ('x', 'X'):
        break

fb.close()