# Guess code game

number = 7
user_input = input('Enter "y" if you would like to play ').lower()


if(user_input == 'y'):
    user_number = int(input('Guess your number:'))
    if(user_number == number):
        print('You guessed correctly!!')
    elif abs(user_number-number) == 1:
        print('You are very close to correct answer')
    else:
        print("Sorry, Game over, it's wrong!!!")
