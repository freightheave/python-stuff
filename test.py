print('How many dogs do you have?')
numDogs=input()
try:
    if int(numDogs)>=4:
        print('That\'s a lot of dogs!')
    elif 0<=int(numDogs)<4:
        print('That\'s an okay number of dogs.')
    else:
        print("You cannot have that number of dogs!")
except:
    print('Invalid Input!')
