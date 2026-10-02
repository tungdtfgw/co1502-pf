username = input('Enter username: ')
password = input('Enter password: ')

if username == '' or password == '':
    print('Invalid username or password')
    exit()

if username == 'admin' and password == '123456':
    print('Login successful')
else:
    print('Incorrect username or password')