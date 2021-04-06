#phoneAndEmail.py - program that takes a wall of text from clipboard, find instances of emails and phone numbers
# and put it back into clipboard.

# 1. Take data from clipboard
# 2. Search for e-mail adresses and phone numbers
# 3. Put each phone number and email into a list
# 4. join everything into a string
# 5. Put it into a clipboard

# Typical phone number in Poland:
# 61 835 15 11
# +48 61 835 15 11
# 601 305 212
# +48 601 305 212
# 61 878 5279
# +48 61 878 5279
# (+48)? 2-3-2-2 /3-3-3 /2-3-4

# Typical e-mail address:
# local-part@domain
# local-part: a-zA-Z0-9!#$%&'*+-/=?^_`{|}~ and . but not consecutively and not
# at the end and beginning, 1-25 signs
# domain: a-zA-Z0-9 and - not at the end beginning
# . 3-25 letters

import re, pyperclip

phoneNumRegex = re.compile(r'''(
    ( \+?\d{2}|\(\+?\d{2}\)(\s|-|\.)? )? # area code
    
    ( \d{2} (\s|-|\.)? \d{3} (\s|-|\.)? \d{2} (\s|-|\.)? \d{2} (\s|-|\.)? |
        \d{3} (\s|-|\.)? \d{3} (\s|-|\.)? \d{3} (\s|-|\.)? |
        \d{2} (\s|-|\.)? \d{3} (\s|-|\.)? \d{4} (\s|-|\.)? )
        # ^9 digits in 2-3-4, 3-3-3, 2-3-2-2 combinations
)''', re.VERBOSE)

emailAddrRegex = re.compile(r'''(
    ( [a-zA-Z0-9!#\$%&'\*\+-/=\?\^_`\{\|\}~]+ ) # local part
    ( @ ) # at sign
    ( [a-zA-Z0-9\.-]+ )?
)''', re.VERBOSE | re.IGNORECASE)

wallOfText = str(pyperclip.paste())
matches = []

mo1 = phoneNumRegex.search(' 61 655 33 00 , 532 795 478')

print(mo1.groups(0))

#for groups in phoneNumRegex.findall(wallOfText):
    #phoneNumber = groups(3)

