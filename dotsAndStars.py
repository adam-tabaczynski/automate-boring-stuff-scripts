import sys, math

def fun_game():
    n = int(input())
    m = int(input())
    zero = [] + [''] * n
    rows = []
    columns = [] + [int('0')] * m

    for i in range(n):
        s=input()
        zero[i]= s
        
    rowCounter = 0
    
    for rowIter in range(len(zero)):        
        for columnIter in range(len(zero[rowIter])):
            if zero[rowIter][columnIter] == '*':
                rowCounter = rowCounter + 1
                columns[columnIter] = int(columns[columnIter]) + 1      
        rows += [rowCounter]
        rowCounter = 0
        
    print("ROWS:")
    for rowStars in rows:
        print(rowStars)

    print("COLUMNS:")
    for columnStars in columns:
        print(columnStars)

fun_game()       
