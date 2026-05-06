import os
print(os.getcwd())
parentDirectory = os.getcwd()
workingDirectory = os.getcwd()+'/learningosmodule'
os.chdir(workingDirectory)
print(os.getcwd())
listOfDirOrFiles = os.listdir()
print(listOfDirOrFiles)
print(f'count of files: {len(listOfDirOrFiles)}')
# Moving to the parent directory 
# Listing the content of parent directory.
print('Listing the content of parent directory:')
os.chdir(parentDirectory)
listOfDirOrFiles = os.listdir()
# print(listOfDirOrFiles)
for file in listOfDirOrFiles:
    print(file)
print(f'count of files: {len(listOfDirOrFiles)}')

os.mkdir('newfolder')

listOfDirOrFiles = os.listdir()
# print(listOfDirOrFiles)
for file in listOfDirOrFiles:
    print(file)
print(f'count of files: {len(listOfDirOrFiles)}')
