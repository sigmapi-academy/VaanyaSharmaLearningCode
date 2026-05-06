
filename = input('Enter file name: ')
with open("FileHandling\\DataFiles\\"+filename+".bin", "rb") as fo:
    content = fo.read()
    
print(content)
print("List format: ", list(content))