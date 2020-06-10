def guess():
    import random
    lucky_number = random.randrange(1, 9)
    guess = int(input('Guess a number: '))

    while guess:
        if lucky_number < guess:
            lucky_number = random.randrange(1, 9)
            guess = int(input('That was too high. Guess again: '))
        elif lucky_number > guess:
            lucky_number = random.randrange(1, 9)
            guess = int(input('That was too low. Guess again: '))
        else:
            lucky_number = random.randrange(1, 9)
            winner_choice = input('   \n   Yaaay, you got it!!!\n \nDo you want to play again?: ')
            if winner_choice == 'no':
                print('\n  Thanks for playing:)\n      Goodbye')
                break
            elif winner_choice == 'yes':
                guess = int(input('\nAwesome! How long before you get it again...\n      Guess a number:'))
guess()