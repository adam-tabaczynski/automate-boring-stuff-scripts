import random

# This one simply prints an inventory from dictionary.
def InventoryPrinter(inventoryDict):
    print("Inventory:")
    sumOfItems = 0
    for item, amount in inventoryDict.items():
        sumOfItems += amount
        print(str(amount) + ' ' + item)
    print('Total number of items: ' + str(sumOfItems))

# This will fill a passed dictionary with items from a list as keys and some random values.
def InventoryFiller(passedInventoryDict, passedItemList):
    for i in range(len(passedItemList)):
        passedInventoryDict[passedItemList[i]] = random.randint(10, 60)

    return passedInventoryDict

# This function adds new stuff to inventory.
def AddToInventory(currentInventoryDict, newItemsList):
    for item in newItemsList:
        currentInventoryDict.setdefault(item, 0)
        currentInventoryDict[item] = currentInventoryDict[item] + 1

    return currentInventoryDict
    

itemList = ['rope', 'torch', 'gold coin', 'arrow']
foundItemsList = ['dragon coin', 'gold coin', 'torch', 'torch', 'sword']

someDict = InventoryFiller({}, itemList)

InventoryPrinter(someDict)

AddToInventory(someDict, foundItemsList)

InventoryPrinter(someDict)
