##guessing the item and won the macth

import random

choices = ['rock', 'paper', 'scissor']

scores = {'player': 0, 'computer': 0}

for round in range(1, 6):
    print('\nRound {round}')


    user_choice = input('Enter you choice rock, paper, scissor or quit?: ')


    if user_choice == 'quit':
        print(f'end the game')
        break

    if user_choice not in choices:
        print(f'Invilad Choice!')  
        continue


    computer_choices = random.choice(choices)
    print(f'Computer Choices: {computer_choices}')

    if user_choice == computer_choices:
        print(f'The Macth in tie')

    elif(user_choice == 'rock' and computer_choices == 'scissor') or \
        (user_choice == 'paper' and computer_choices == 'rock') or \
        (user_choice == 'scissor' and computer_choices == 'paper'):
        print(f'You win the round')
        scores['player'] += 1
    else:
        print(f'computer win')
        scores['computer'] += 1

print('\nFinal Scores: ')
print(f'You: {scores['player']} | Computer: {scores["computer"]}')

if scores['player'] == scores['computer']:
    print("Oh the macth tie")
elif scores['player'] > scores['computer']:
    print("Wow, You Win")
else:
    print('Computer win') 