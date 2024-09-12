print('Welcome to my computer quiz!')

playing = input('Would you like to play a game (yes/no)? ')

if playing.lower() != 'yes':
    quit()

print("Okay!! Let's play :)")
score = 0

questions_answers = {'What does CPU stard for? ': 'central processing unit',
                    'What does GPU stard for? ': 'graphics processing unit',
                    'What does RAM stard for? ': 'random access memory',
                    'What does PSU stard for? ': 'power supply unit'
}

for question, answer in questions_answers.items():
    user_answer = input(question)
    if user_answer.lower() == answer:
        print('Nice job!')
        score += 1
    else:
        print('Baaaah!')   

print(f'You got {score} question our of {len(questions_answers)} correct!')
print(f'You got {100*score/len(questions_answers)}%')