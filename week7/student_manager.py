students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack']
grades = [85, 92, 78, 30, 88, 35, 82, 89, 91, 87]

def main():
    running = True

    while running:
        print_menu()
        choice = input('Enter your choice (1-5): ')
        if choice == '1':
            print_students(students, grades)
        elif choice == '2':
            print_pass(students, grades)
        elif choice == '3':
            print_best(students, grades)
        elif choice == '4':
            st_name = input('Enter student name: ')
            find_student(students, grades, st_name)
        elif choice == '5':
            running = False
        else:
            print('Invalid choice. Please try again.')

def print_menu():
    print('TODO later')

def print_students(students, grades):
    print('TODO later') 

def print_pass(students, grades):
    print('TODO later')

def print_best(students, grades):
    print('TODO later')

def find_student(students, grades, st_name):
    print('TODO later')

## MAIN
main()