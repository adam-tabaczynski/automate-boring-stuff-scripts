#! python3
# bulletPointAdder.py - add a star and space at the beginning of each line for text in clipboard

import sys, pyperclip

print('Copied text: \n' + pyperclip.paste())
copiedText = pyperclip.paste().split('\r\n')

for index, text in enumerate(copiedText):
    copiedText[index] = '* ' + text

newText = '\r\n'.join(copiedText)

print('\nModified text: \n' + newText)
pyperclip.copy(newText)
print('\nText added to clipboard.')
