# Checks if given chess board is valid
# Each player has: 0-16 pieces, 0-8 pawns, 1 king
# name of the keys: 1a, 1b 1c, ... 1h, 2a, 2b, ... 8g, 8h.
# 'w' or 'b' at the start means white or black

def GenerateFields(chessboard):
    charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(8):
        for currentChar in charList:
            field = str(i + 1) + currentChar
            chessboard.setdefault(field, ' ')

def CheckFieldsValidity(chessboard):
    charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(8):
        for currentChar in charList:
            field = str(i + 1) + currentChar
            if field not in chessboard.keys():
                return "Field differs from 1a - 8h system."
    return "All fields are good."

def CheckPieces(chessboard):
    if 'wking' in chessboard.values() and 'bking' in chessboard.values():
        wkingCounter = 0
        bkingCounter = 0
        wpawnsCounter = 0
        bpawnsCounter = 0
        wpiecesCounter = 0
        bpiecesCounter = 0
        for field, piece in chessboard.items():
            if piece == ' ':
                continue
            if piece[0] == 'w':
                if piece[1:] == 'king':
                    wkingCounter += 1
                    wpiecesCounter += 1
                    if wkingCounter > 1:
                        return "More than 1 white king has been found."
                    
                elif piece[1:] == 'pawn':
                    wpawnsCounter += 1
                    wpiecesCounter += 1
                    if wpawnsCounter > 8:
                        return "More than 8 white pawns have been found."
                    
                elif pieces[1:] == 'rook' or pieces[1:] == 'knight' or pieces[1:] == 'bishop' or pieces[1:] == 'queen':
                    wpiecesCounter += 1
                    
                else:
                    return "Wrong white piece: " + piece + " has been found on " + field + " field."

                if wpiecesCounter > 16:
                    return "More than 16 white pieces have been found."
                
            elif piece[0] == 'b':
                if piece[1:] == 'king':
                    bkingCounter += 1
                    bpiecesCounter += 1
                    if bkingCounter > 1:
                        return "More than 1 black king has been found."
                    
                elif piece[1:] == 'pawn':
                    bpawnsCounter += 1
                    bpiecesCounter += 1
                    if bpawnsCounter > 8:
                        return "More than 8 black pawns have been found."
                    
                elif pieces[1:] == 'rook' or pieces[1:] == 'knight' or pieces[1:] == 'bishop' or pieces[1:] == 'queen':
                    bpiecesCounter += 1
                    
                else:
                    return "Wrong black piece: " + piece + " has been found on " + field + " field."

                if wpiecesCounter > 16:
                    return "More than 16 white pieces have been found."
            else:
                return "Wrong first character of " + piece + " from " + field + " field."
            
        return "All is fine with pieces."
            

    else:
        return "Lack of white or black king have been found."


testChessboard = {}
GenerateFields(testChessboard)
testChessboard['1a'] = 'wking'
testChessboard['8h'] = 'bking'

print(CheckFieldsValidity(testChessboard))
print(CheckPieces(testChessboard))
