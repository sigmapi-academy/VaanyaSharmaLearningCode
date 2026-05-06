import pickle

student1 = {
    "name": "Jacob",
    "age": 17,
    "marks":[55, 70, 98]
}

filename = input('Enter your file name: ')
with open("FileHandling/DataFiles/" + filename + ".dat", "ab") as fo:
    pickle.dump(student1, fo)

print("New object appended")