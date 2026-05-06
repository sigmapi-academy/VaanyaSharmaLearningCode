import pickle

filename = input('Enter your file name: ')
with open("FileHandling/DataFiles/" + filename + ".dat", "rb") as fo:
    while True:
        try:
            stud1 = pickle.load(fo)
            print(stud1)
            print('-'*70)
        except EOFError:
            print('End of file')
            print('-'*70)
            break