import pickle

student1 = {
    "name": "Jhon",
    "age": 18,
    "marks":[85, 90, 88]
}

filename = input('Enter your file name: ')
with open("FileHandling/DataFiles/" + filename + ".dat", "wb") as fo:
    pickle.dump(student1, fo)

print("Object stored in the file")