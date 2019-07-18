
def passwordFunction():
    print('Username: ')
    user = input()
    print('Password: ')
    password = input()
    if user == 'shaydamoezzi':
        if password == 'password':
            print('access granted')
    else:
        print('access denied')

passwordFunction()
