# English to Pig Latin

print('Enter the English message to translate into Latin Pig.')
message = input()

message = message.split(' ')
print(message)
newMessage = []

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

for i in range(len(message)):
    sign = ''

    if message[i][-1] in ('.', ','):
        sign = message[i][-1]
        message[i] = message[i][:-1]

    # skip actions if it is a number.
    if message[i][0].isdecimal():
        continue
    
    # if word starts with a vowel, add 'yay' at the end
    elif message[i][0].lower() in VOWELS:
        if message[i][0].isupper() and len(message[i]) > 1:
            message[i] += 'YAY'
        else:    
            message[i] += 'yay'

    # if word starts with a consonant, move first letter to the end and add 'ay'
    else:
        if message[i].istitle():
            if len(message[i]) > 2:
                if message[i][1].lower() not in VOWELS:
                    message[i] = (message[i][2:] + message[i][0:2].lower() + 'ay').title()
                else:
                    message[i] = (message[i][1:] + message[i][0].lower() + 'ay').title()
            else:
                message[i] = message[i][1].upper() + message[i][0].lower() + 'ay'
                
        elif message[i].isupper():
            if message[i][1].lower() not in VOWELS:
                message[i] = message[i][2:] + message[i][0:2] + 'AY'
            else:
                message[i] = message[i][1:] + message[i][0] + 'AY'
        else:
            if message[i][1].lower() not in VOWELS:
                message[i] = message[i][2:] + message[i][0:2] + 'ay'
            else:
                message[i] = message[i][1:] + message[i][0] + 'ay'
    message[i] += sign

newMessage = ' '.join(message)
print(newMessage)

