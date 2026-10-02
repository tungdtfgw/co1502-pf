n = int(input('Enter day of the week (1-7): '))

if n < 1 or n > 7:
    print('Invalid day of the week')
    exit()

status = 'Workday - go to school/work'

if n == 1:
    day = 'Sunday'
    status = 'Weekend - go out!'
elif n == 2:
    day = 'Monday'
elif n == 3:
    day = 'Tuesday'
elif n == 4:
    day = 'Wednesday'
elif n == 5:
    day = 'Thursday'
elif n == 6:
    day = 'Friday'
elif n == 7:
    day = 'Saturday'
    status = 'Weekend - go out!'

print(f'{day}: {status}')