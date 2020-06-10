password = 'passwo'
message = ' "I will bring cookies tomorrow"'
close = 'pass'
closer = 'passw'
guess = input('type password: ')

while (password!= guess):
    if guess == close:
        print('very close')
    if guess == closer:
        print('very very close')
    print('wrong')
    guess = input('type password: ')
while (password==guess):
    print('great job. you have unlocked a message. it reads' + message)
    break

experience = input('Did you have a good experience?:')

while (experience != 'yes'):
    if experience == 'no':
        experience = input('sorry. we will make it better. okay?:')
    else:
        print('its okay')
        break
while (experience == 'yes'):
    print('wooow')
    break
