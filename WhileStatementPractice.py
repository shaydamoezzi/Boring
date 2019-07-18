print('Enter your password')
password = input()
correctpass = 'rightpassword'
if password == correctpass:
    print('Access granted')
while password != correctpass:
    print('Try again: ')
    password = input()
print('Access granted')

while True: #this creates an infinite loop
    print('What is your name?')
    name = input()
    if name == 'Shayda':
        break #this will break out of the loop if the stated conditions are met
print('Thank you and welcome!')
