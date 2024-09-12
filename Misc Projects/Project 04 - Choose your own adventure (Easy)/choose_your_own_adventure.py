user_name = input('What is your name adventurer? ')
print(f'Welcome {user_name} to this adventure')

answer = input('You are on a dirt road, it has come to an end. You can go left or right. Which way would you like to go (left/right)? ').lower()

if answer == 'left':
    answer = input('You come to a river. You can walk around it or swim accross (walk/cross): ' ).lower()
    if answer == 'swim':
        print('You swam accros and was eaten by an alligator')
    elif answer == 'walk':
        print('You walked for many miles and ran out of water. You lost the game')
    else:
        print('Not a valid answer. You lose!!')
elif answer == 'right':
    answer = input('You found a bridge. It looks wobbly. Do you want to cross it or head back (cross/back)? ').lower()
    if answer == 'cross':
        answer = input('You crosses the bridge and meet a stranger. Do you talk to him (yes/no)? ').lower()
        if answer == 'yes':
            print('You found the person you were looking for. You win the game')
        if answer == 'no':
            print('You wonder forever looking for the Hermit. You lose.')
        else:
            print('Not a valid answer. You lose!!')
    elif answer == 'back':
        print('You go back to the main road...')
    else:
        print('Not a valid answer. You lose!!')
else:
    print('Not a valid answer. You lose!!')
    quit()

print(f'Thank you for trying {user_name}')