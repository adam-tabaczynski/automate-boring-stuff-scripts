catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) +1) + ' (Or enter nothing to stop.):')
    catName = input()

    if catName == '':
        break
    catNames += [catName]

print('The cat names are:')
for name in catNames:
    print(name)
