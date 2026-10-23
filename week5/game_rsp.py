# Game Rock Scissors Paper
import random as rd

def game_play():
    playing = True
    while playing:
        player_choice = get_player_choice()
        comp_choice = get_computer_choice()
        result = compare(player_choice, comp_choice)
        print(f'You: {player_choice}')
        print(f'Computer: {comp_choice}')
        print(f'Result: {result}')

        playing = is_continue()

    print('Game ended. Thanks for playing!')

def get_player_choice():
    choice = input('Enter your choice (r/s/p): ')
    return choice

def get_computer_choice():
    choice = rd.randint(1, 3)    # sinh ra 1 số nguyên ngẫu nhiên từ 1 đến 3
    return 'r' if choice == 1 else 's' if choice == 2 else 'p'

def compare(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'Draw'

    if player_choice == 'r' and computer_choice == 's':
        return 'Win'

    if player_choice == 's' and computer_choice == 'p':
        return 'Win'

    if player_choice == 'p' and computer_choice == 'r':
        return 'Win'

    return 'Lose'

def is_continue():
    choice = input('Do you want to continue? (y/n): ')
    return choice.lower() == 'y'


# Call main function to start the game
game_play()