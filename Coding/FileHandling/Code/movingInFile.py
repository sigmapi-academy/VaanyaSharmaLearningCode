
with open("FileHandling/DataFiles/Marks.txt", "rb") as fo:
    fo.seek(-15,2)
    line = fo.read(15)
    print("Last 15 bytes of file contain:", line)