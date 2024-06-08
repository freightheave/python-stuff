# This is a number guessing game.
import random

def guess():
    secret_num = random.randint(1,20)
    i=1
    while i<6:
        print('Take a guess!')
        try:
            i+=1
            num=int(input())
            if num < secret_num:
                print('Your guess is too low.')
            elif num > secret_num:
                print('Your guess is too high.')
            elif num == secret_num:
                break
        except:
            print('Enter a number!')
            break
    if num == secret_num:
        print('Yup! '+str(num)+' is the correct guess. You guessed the number in '+str(i-1)+' tries.')
    else:
        print('Nope. The answer is '+str(secret_num)+'.')


print('Hello there! What is your name?')
name = input()
print('Hi '+name+'. Do you want to take a guess at the number I\'m thinking of?')
user_decision=input()
if user_decision == 'Yes' or user_decision == 'yes' or user_decision == 'Y' or user_decision == 'y':
    print('Noice!')
    guess()
elif user_decision == 'No' or user_decision == 'no' or user_decision == 'N' or user_decision == 'n':
    print('NVM, You can try anytime again!')
else:
    print('Try again.')
input()
