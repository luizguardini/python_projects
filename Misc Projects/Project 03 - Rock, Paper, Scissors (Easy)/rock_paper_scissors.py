import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock/Paper/Scissors or "Q" to quit: ').lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        print('Wrong input!')
        continue

    computer_pick = random.sample(options,1)[0]
    print(f'Computer picked {computer_pick}.')

    if (user_input == 'rock') and (computer_pick == 'scissors'):
        print('You won!')
        user_wins += 1
    elif (user_input == 'paper') and (computer_pick == 'rock'):
        print('You won!')
        user_wins += 1
    elif (user_input == 'scissors') and (computer_pick == 'paper'):
        print('You won!')
        user_wins += 1    
    elif (user_input == computer_pick):
        print('Draw!')   
    else:
        print('You lost!')
        computer_wins += 1

print(f'Score: You {user_wins} X {computer_wins} Computer')       

print('Goodbye!')

    