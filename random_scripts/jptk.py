# jptk.py - creates a batch of text files named with a single letter from given user's input

from pathlib import Path
import pyinputplus as pyip


user_input = pyip.inputStr(prompt='Enter a sentence:\n')
filesFolder = (Path.cwd() / 'jptk_test')

for index, letter in enumerate(user_input):
    letter_file = open(f'{str(filesFolder)}\\000{index}_{letter}.txt', 'w')
    letter_file.close()
