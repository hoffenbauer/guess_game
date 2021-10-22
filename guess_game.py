from random import shuffle
from number_choice import number_validation

ball_list = ['', 'O', '']
shuffle(ball_list)

choice = number_validation(0,3)

if ball_list[choice] == 'O':
    print(f'Congratulations!')
    print(ball_list)
else:
    print(f"Too bad! The ball was at position {ball_list.index('O')}!")
    print(ball_list)
