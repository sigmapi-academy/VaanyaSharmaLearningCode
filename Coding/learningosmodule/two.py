import os

# os.makedirs('A/B/C')

# os.rmdir('newfolder')

# os.removedirs('A/B/C')

cwd = os.getcwd()+'\\'
pth = os.path.join(cwd+'learningosmodule','three.py')
print(pth)

# with open(path, 'w') as fo:
#     pass

# isPathExist = os.path.exists(pth)
# if isPathExist:
#     print('yes')
# else:
#     print('no')

pwd = os.getcwd()
isFile = os.path.isfile(pth)
isDir = os.path.isdir(pwd)
print(isFile)
print(isDir)
print(pth)
print(pwd)