# tablePrinter.py - program that takes list of lists of strings and display it in table with
#   each column right justified.


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(nestedTable):
    
    for list_ in nestedTable:
        
        maxLengthOfWord = 0

        # Finds word of maximum length and saves it to var.
        for nestedListIndex in range(len(list_)):
            if maxLengthOfWord < len(list_[nestedListIndex]):
                maxLengthOfWord = len(list_[nestedListIndex])

        # Justifies the tex based on highest length of word in a list.
        for nestedListIndex in range(len(list_)):
            list_[nestedListIndex] = list_[nestedListIndex].rjust(maxLengthOfWord)

    # Prints the table in given format.       
    for nestedListIndex in range(len(list_)):
        for listIndex in range(len(nestedTable)):
            print(nestedTable[listIndex][nestedListIndex] + ' ', end='')
    
        print()


printTable(tableData)
