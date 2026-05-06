
with open("FileHandling/DataFiles/Marks.txt", "r") as fo:
    print("initial position of the file pointer:", fo.tell())
    print("3 bytes read are:", fo.read(3))
    print("After previous read, current position of the file pointer:", fo.tell())
    print("next 4 bytes read are:", fo.read(4))
    print("After previous read, current position of the file pointer:", fo.tell())