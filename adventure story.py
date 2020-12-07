name = input('What is your name?:')
print(f'Hello {name.capitalize()}, you are about to go on an adventure. You enter a room and see two doors. One is red and the other blue.')
door_input = input('which door do you choose?: ')
if door_input == 'red':
    print('Red door leads you to the future. You have to help a scientist to get back.')
    help = input('Do you help?: ')
    if help == 'yes':
        print('Awesome, the scentist will help you get back')
    elif help == 'no':
        print('what? now you are stuck in the future forever. Game over.')
elif door_input == 'blue':
    print('Blue dooor leads to the past. You have to help a wizard, who will help you get back')
    wizard_help = input('will you help the wizard?: ')
    if wizard_help == 'yes':
        print('yaaay you get back')
    elif wizard_help == 'no':
        print ('omg. what were you thinking? now you have to steal his saber to escape.')
        steal = input('would you steal or leave?: ')
        if steal == 'steal':

            print('good choice. now run and use it to escape. good luck')
        elif steal == 'leave':
            print('woow you must know a way out. good luck.')
