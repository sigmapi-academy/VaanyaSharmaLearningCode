
filename = input('Enter file name: ')
with open("FileHandling\\DataFiles\\"+filename+".bin", "wb") as fo:
    numbers = [n for n in range(10, 60, 10)]
    data = bytes(numbers)
    fo.write(data)
    
    