import pyinputplus as pyip
import sys

def idiot_keeper():
    user_input = ''
    while True:
        print('You want to know how to keep an idiot busy for hours?')
        user_input = pyip.inputYesNo()
        if user_input == 'no':
            break


idiot_keeper()
