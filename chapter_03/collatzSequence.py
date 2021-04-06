# Program that uses collatz sequence, that bring a given number to a 1 via some statements
# I tried to put everything into functions for clarity

def Collatz(number):
    if number%2 == 0:
        print(number//2)
        return number//2
    elif number == 1:
        return 1
    else:
        print(3*number+1)
        return 3*number+1

def CollatzLoop(number):
    while True:
        number = Collatz(int(number))
        if number == 1:
            print('Finally, we are at 1!')
            break
        
def WelcomeBanner():
    print('Welcome to collatz sequence!')
    print('Pass in an integer:')
    userInput = ''
    while True:
        userInput = input()
        try:
            parsedValue = int(userInput)
            return parsedValue
        except ValueError:
            print('That is not an integer, please type in an integer.')

def EndingBanner():
    print("Wanna try with a different number? Type 'n' if no, type in anything except 'n' if yes")
    userInput = input()
    return userInput

def GameLoop():
    result = '' 
    while result != 'n':
        userInput = WelcomeBanner()
        
        CollatzLoop(userInput)

        result = EndingBanner()

GameLoop()
