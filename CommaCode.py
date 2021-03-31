def listToStringWithCommas(passedList):
    if len(passedList) == 0:
        return "Wypad mi z tom pustom listo"
    resultString = ''
    for index in range(len(passedList)):
        resultString += passedList[index]

        if index == len(passedList) - 1:
            break
        elif index == len(passedList) - 2:
            resultString = resultString + ' and '
        else:
            resultString = resultString + ', '

    return resultString

testList = ['janek', 'dzbanek', 'bananek', 'baranek']
print(listToStringWithCommas(testList))
emptyList = []
print(listToStringWithCommas(emptyList))
