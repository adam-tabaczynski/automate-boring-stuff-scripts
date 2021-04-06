import random, sys

def HelloBanner(wins, losses, ties):
    print('ROCK, PAPER, SCISSORS')
    print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')

def UserInputBanner():
    print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit.')
    while True:
        userInput = input()
        if userInput == 'q':
            sys.exit()
        if userInput == 'p' or userInput == 'r' or userInput == 's':
            break
        print('Type in r, p, s or q.')
    return userInput

def GenerateMove():
    numberGenerated = random.randint(1,3)
    if numberGenerated == 1:
        return 'r'
    elif numberGenerated == 2:
        return 'p'
    else:
        return 's'

def GameRPS():
    wins = 0
    losses = 0
    ties = 0
    while True:
        HelloBanner(wins, losses, ties)
        userSign = UserInputBanner()
        machineSign = GenerateMove()
        if userSign == 'r' and machineSign == 'r':
            print('ROCK versus... ')
            print('ROCK')
            print('It is a tie!')
            ties += 1
        elif userSign == 'r' and machineSign == 'p':
            print('ROCK versus... ')
            print('PAPER')
            print('You lose!')
            losses += 1
        elif userSign == 'r' and machineSign == 's':
            print('ROCK versus... ')
            print('SCISSORS')
            print('You win!')
            wins += 1
        elif userSign == 'p' and machineSign == 'r':
            print('PAPER versus... ')
            print('ROCK')
            print('You win!')
            wins += 1
        elif userSign == 'p' and machineSign == 'p':
            print('PAPER versus... ')
            print('PAPER')
            print('It is a tie!')
            ties += 1
        elif userSign == 'p' and machineSign == 's':
            print('PAPER versus... ')
            print('SCISSORS')
            print('You lose!')
            losses += 1
        elif userSign == 's' and machineSign == 'r':
            print('SCISSORS versus... ')
            print('ROCK')
            print('You lose!')
            losses += 1
        elif userSign == 's' and machineSign == 'p':
            print('SCISSORS versus... ')
            print('PAPER')
            print('You win!')
            wins += 1
        elif userSign == 's' and machineSign == 's':
            print('SCISSORS versus... ')
            print('SCISSORS')
            print('It is a tie!')
            ties += 1
        else:
            print('Something is not alright.') 

GameRPS()
