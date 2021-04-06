# for a given folder path, crawler check each file if it have '.pdf' or '.jpg'
# extension, and then copies it to new folder.

import os, shutil

def get_images_to_one_place(folder):
  destination_folder = 'C:\\Users\\adamt\\Desktop\\found_images'
  extensions_tuple = ('.jpg', '.jpeg', 'pdf', '.png')
  folder = os.path.abspath(folder)
  
  for foldername, subfolders, filenames in os.walk(folder):
    if foldername == destination_folder:
      continue
    print(f'Adding files in {os.path.basename(foldername)}...')
    
    for filename in filenames:
      if filename.endswith(extensions_tuple):
        print(os.path.join(foldername, filename))
        print(destination_folder)
        shutil.copy(os.path.join(foldername, filename), destination_folder)
        
get_images_to_one_place('C:\\Users\\adamt\\Desktop')