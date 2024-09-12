# Roll a die and add the number. If roll = 1, ends turn and resets score.
import random

def roll(min_value = 1, max_value = 6):
    return random.randint(min_value, max_value)


while True:
    players = input('Enter the number of players (2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Must be between 2 and 4 players')
    else:
        print('Invalid entry. Please try again')

while True:
    max_score = input('Enter winning score: ')
    if max_score.isdigit():
        max_score = int(max_score)
        if max_score > 0:
            break
        else:
            print('Must be greater than 0')
    else:
        print('Invalid entry. Please try again')

player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        print(f'\nPlayer {player_idx + 1} turn has just started')
        print(f'    Your total score is {player_scores[player_idx]}')
        current_score = 0
        while True:
            should_roll = input('    Would you like to roll (y)? ').lower()
            if should_roll != 'y':
                break

            value = roll()
            if value == 1:
                print('    You rolled 1! Turn done!')
                player_scores[player_idx] = 0
                break
            else:
                player_scores[player_idx] += value
                print(f'    You rolled a {value}')
            print(f'    Your score is {player_scores[player_idx]}')
        print(f'    Your total score is {player_scores[player_idx]}')

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)

print(f'Player {winning_idx+1} is the winner with a score of {max_score}')