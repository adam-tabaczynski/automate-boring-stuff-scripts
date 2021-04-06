import random

machineGuess  = random.randint(1,20)
userGuess = ''
guessCounter = 0
print ('I am thinking of a number between 1 and 20.')

while userGuess != machineGuess:
    print('Take a guess')
    userGuess = input()
    guessCounter += 1
    if int(userGuess) > machineGuess:
        print('Your guess is too high.')
    elif int(userGuess) < machineGuess:
        print('Your guess is too low.')
    elif int(userGuess) == machineGuess:
        print('Good job! You guessed my number in ' + str(guessCounter) + ' guesses!')
        break
        

