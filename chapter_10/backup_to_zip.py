#! python3
# backup_to_zip.py - copies an entire folder and its contents into
# a zip file whose filename increments.

import zipfile, os

def backup_to_zip(folder):
  # Back up the entire contents of "folder" into a ZIP file.
  
  folder = os.path.abspath(folder) # makes sure that folder is absolute
  
  # Figure out the filename this code should use based on
  # what files already exist.
  number = 1
  while True:
    zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
    if not os.path.exists(zip_filename):
      break
    number += 1
    
  # TODO: Create the zip file.
  print(f'Creating {zip_filename}...')
  backup_zip = zipfile.ZipFile(zip_filename, 'w')
  
  # TODO: Walk the entire folder tree and compress the files in each folder.
  for foldername, subfolders, filenames in os.walk(folder):
    print(f'Adding files in {foldername}...')
    # Add current folder to the zip file.
    backup_zip.write(foldername)
    
    # Add all the files in this folder to the zip file.
    for filename in filenames:
      new_base = os.path.basename(folder) + '_'
      if filename.startswith(new_base) and filename.endswith('.zip'):
        continue # do not back up the backup zip files.
      backup_zip.write(os.path.join(foldername, filename))
      
  backup_zip.close()
  print('Done.')
  
backup_to_zip('C:\\Users\\adamt\\automate-boring-stuff-scripts')