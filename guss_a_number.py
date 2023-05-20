import random
computer_number = random.randint(1, 100)
while True:
    player_input = input('Guess the number (1-100):')
    if not player_input.isdigit():
        print('Invalid input. Try again...')
        continue
    player_number = int(player_input)
    if player_number == computer_number:
        print('You guess it!')
        play_again = input('Do you want to play again? (Y/N)')
        if play_again.upper() == 'N':
            break
        if play_again.upper() == 'Y':
            computer_number = random.randint(1, 100)
            continue
    elif player_number > computer_number:
        print('Too High!')
    elif player_number < computer_number:
        print('Too Low!')