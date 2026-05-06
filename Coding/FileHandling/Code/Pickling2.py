import pickle

filename = input('Enter your file name: ')
with open("FileHandling/DataFiles/" + filename + ".dat", "rb") as fo:
    stud1 = pickle.load(fo)

print(stud1)