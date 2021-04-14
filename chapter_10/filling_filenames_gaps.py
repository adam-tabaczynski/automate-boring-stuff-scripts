#! python3
# filling_filenames_gaps.py - program that find all files with given prefix and extension
# and locates any gap with numbering (ex. spam001.txt, spam002.txt, spam004.txt -
# no spam003.txt file) and rename all the later files to close this gap.

import os, re, shutil
import pyinputplus as pyip

# User gives prefix
# User gives extension
# Program finds all instances of given prefix + numbering + extension
# Program gets minimal number value, starts naming from that one.

def filling_filenames_gaps(folder):
  
  folder = os.path.abspath(folder)
  destination_folder = 'C:\\Users\\adamt\\automate-boring-stuff-scripts\\chapter_10\\filled_filenames_files'
  
  print('Welcome to the filenames numbering filler program!')
  print('Type in prefix and extension of a file, example: you have a files')
  print('called spam(yyy).txt - (yyy) is some numbering, "spam" is a prefix')
  print('and ".txt" is an extension.\n')
  
  file_prefix = pyip.inputStr(prompt='Enter a prefix: ')
  file_extension = pyip.inputStr(prompt='Enter an extension: ', 
                                 blockRegexes=[r'.*'],
                                 allowRegexes=[r'\.\w+'])
  
  numbering_regex = re.compile(r'\d+')
  minimal_numbering = 0
  current_numbering = 0
  missed_numberings = 0
  size_of_numbering = 0
  
  print("\n---")
  for index, filename in enumerate(os.listdir(folder)):
        
    # checks if given file starts with a given prefix, end with a given extension
    # and if it contains any digits.
    if (filename.startswith(file_prefix) and 
        filename.endswith(file_extension) and 
        numbering_regex.search(filename)):
                                              
      print('File found: ' + filename)
      mo = numbering_regex.search(filename)
      if index == 0:
        minimal_numbering = int(mo.group())
        current_numbering = int(mo.group())
        size_of_numbering = len(mo.group())
        
      if int(mo.group()) < minimal_numbering:
        minimal_numbering = int(mo.group())
        
      if int(mo.group())  != current_numbering:   
        current_numbering = int(mo.group())
        missed_numberings += 1
        
    current_numbering += 1
        
  print('\nProgram has found ' + str(missed_numberings) + ' gaps in files numbering.') 
  print('Starting number: ' + str(minimal_numbering))
  print('Fixing the numbering of found files...')
  print("\n---")
  current_numbering = minimal_numbering
  for index, filename in enumerate(os.listdir(folder)):
    new_filename = ''
    if (filename.startswith(file_prefix) and 
        filename.endswith(file_extension) and 
        numbering_regex.search(filename)):
      if index == 0:
        current_numbering = minimal_numbering                                                                              
      new_filename = file_prefix + str(current_numbering).zfill(size_of_numbering) + file_extension
    
    current_numbering += 1
    print(new_filename)
    shutil.copy(os.path.join(folder, filename),
                os.path.join(destination_folder, new_filename))
  
# Checks if there continuation - finds minimal, plus one from that
# Checks number of gaps - counter all encounter of files, starting from minimal, change all occurences


filling_filenames_gaps('C:\\Users\\adamt\\automate-boring-stuff-scripts\\chapter_10\\missing_filenames_files')