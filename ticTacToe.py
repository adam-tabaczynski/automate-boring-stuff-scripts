
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}



def PrintBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----+-----+-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----+-----+-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def WelcomeBanner():
    showOffBoard = {'top-L': 'top-L', 'top-M': 'top-M', 'top-R': 'top-R',
            'mid-L': 'mid-L', 'mid-M': 'mid-M', 'mid-R': 'mid-R',
            'low-L': 'low-L', 'low-M': 'low-M', 'low-R': 'low-R'}
    print('Welcome to the tic tac toe game')
    print('For now, user starting the game has Xs')
    print('This is a board with name of each field. To put a sign in field, type in the name of a field.')
    printBoard(showOffBoard)

while True:
    while 
    print('X turn')
    
    print(theBoard)
    



