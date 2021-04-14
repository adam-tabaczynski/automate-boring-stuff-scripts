# madLibs.py - program that reads text file and let user add their own text anywhere the word
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
from pathlib import Path
import time
import re
import pyinputplus as pyip
import time

# This creates a path to folder separated for this project
filesFolder = (Path.cwd() / 'chapter_09\\madLibsTexts')

# Regexes created to found given word
# and to found if currently checked word ends with a . , or some other sign.
libs_regex = re.compile(r'^ADJECTIVE|^NOUN|^ADVERB|^VERB')
letter_regex = re.compile(r'\W')

template_file = open(f'{str(filesFolder)}\\basic_text.txt', 'r')
template_file_content = template_file.read()
list_of_separated_words = template_file_content.split()

for index, word in enumerate(list_of_separated_words):
    matching_word = libs_regex.search(word)

    # If given word is found, it prompts user to type in word the user sees as correct.
    if matching_word != None:        
        user_input = pyip.inputStr(prompt='Enter ' + matching_word.group().lower() + ':\n')

        # Checks if a word ends with a . or , or some other sign.
        # If yes, then puts it at the end of the new word.
        if letter_regex.search(word[-1]):
            user_input = user_input + word[-1]
            
        list_of_separated_words[index] = user_input

new_string = ' '.join(list_of_separated_words)

# timestamp generated for file name.
timestamp_note = int(time.time())

# New file is created. To differ between new files, timestamp is added to its name.
end_file = open(f'{str(filesFolder)}\\filled_text{timestamp_note}.txt', 'w')
end_file.write(new_string)

template_file.close()
end_file.close()


        
# find each occurence of said words - regex? ^ADJECTIVE | ^N
# for each occurence, show input prompt so it can be chanded
# print the whole thing
# save it to new text file
