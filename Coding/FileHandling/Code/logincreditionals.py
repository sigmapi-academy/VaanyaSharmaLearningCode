# Develop a secure storage program:
# 	• Store username and password in binary file
# 	• Allow login verification
# 	• Count login attempts
# Display locked users after 3 failed attempts

import pickle


while True:
    print('Press 1 to sign in')
    print('Press 2 to log in')
    print('Press 0 to exit')
    ch = int(input('Enter your choice: '))
    match ch:
        case 1:
            with open("FileHandling/DataFiles/users.dat", 'ab') as fo:
                email = input('Enter your email as user name: ')
                password = input('Enter your password: ')
                user = {email:password}
                pickle.dump(user, fo)
        case 2:
            with open("FileHandling/DataFiles/users.dat", 'rb') as fo:
                userName = input('Enter email as user name: ')
                liOfUsers=[]
                obj={}
                try:
                    while True:
                        obj = pickle.load(fo)
                        liOfUsers.append(obj)
                except EOFError:
                    count = 0
                    for li in liOfUsers:
                        uname = list(li.keys())
                        pwd = list(li.values())
                        if uname[0] == userName:
                            while count < 3:
                                password = input('Enter your password: ')
                                if pwd[0] == password:
                                    print('You are logged in successfully...')
                                    break
                                else:
                                    count += 1
                            if count == 3:
                                print('You have entered wrong password for three times,')
                                print('Your account is blocked for 24 hours.')
        case 0:
            exit()      
                