def WelcomeBanner():
    print('Type in number of values you will write into program (More than 1, less then 10).')
    while True:
        numbersAmount = input()
        numbersAmount = int(numbersAmount)
        if numbersAmount >= 1 and numbersAmount <= 10:
            return numbersAmount
        else:
            print('That is number outside of the scope 1 and 10, please try again.')

def NumbersInput(passedNumbers):
    numbersList = []
    for i in range(passedNumbers):
        print(f'Type in {i + 1}. number')
        userNumber = input()
        numbersList.append(int(userNumber))
        
    print('')
    return numbersList

def PrintWithRemovedSignificantBit(passedList):
    for i in passedList:
        print(int(bin(i)[3:], 2))

def RemSigBit():
    usersNumberAmount = WelcomeBanner()
    userNumbersList = NumbersInput(usersNumberAmount)
    PrintWithRemovedSignificantBit(userNumbersList)

RemSigBit()
