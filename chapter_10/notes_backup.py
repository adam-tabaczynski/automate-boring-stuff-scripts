import zipfile, os, datetime

def get_current_date():
  current_date = datetime.datetime.now()
  year = str(current_date.year)[2:]
  if current_date.month < 10:
    month = '0' + str(current_date.month)
  else:
    month = str(current_date.month)
    
  if current_date.day < 10:
    day = '0' + str(current_date.day)
  else:
    day = str(current_date.day)
    
  return day + '_' + month + '_' + year

def notes_backup(folder):
  
  today = get_current_date()
  folder = os.path.abspath(folder)
  
  # Checks if there was a backup done on the same day
  while True:
    zip_filename = 'notes_' + today + '.zip'
    if not os.path.exists(zip_filename):
      break
    
    
  print(f'Creating {zip_filename}...')
  backup_zip = zipfile.ZipFile(zip_filename, 'w')
        
  for foldername, subfolders, filenames in os.walk(folder):
    if not '.git' in foldername and not 'node_modules' in foldername:
      print(f'Checking for files in {foldername}...')
      for filename in filenames:
        if 'notes' in filename and filename.endswith('.txt'):
          print(filename)
          backup_zip.write(os.path.join(foldername, filename), filename)
      
  backup_zip.close()
  print('Done.')
  
notes_backup('C:\\Users\\adamt\\Desktop')