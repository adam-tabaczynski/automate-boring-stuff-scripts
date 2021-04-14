import zipfile, os

def python_backup(folder):
  
  folder = os.path.abspath(folder)
  
  number = 1
  while True:
    zip_filename = 'python_' + os.path.basename(folder) + '_' + str(number) + '.zip'
    if not os.path.exists(zip_filename):
      break
    number += 1
    
    
  print(f'Creating {zip_filename}...')
  backup_zip = zipfile.ZipFile(zip_filename, 'w')
        
  for foldername, subfolders, filenames in os.walk(folder):
    print(f'Adding files in {foldername}...')
    
    for filename in filenames:
      if filename.endswith('.py'):
        print(filename)
        backup_zip.write(os.path.join(foldername, filename), filename)
      
  backup_zip.close()
  print('Done.')
  
python_backup('C:\\Users\\adamt\\automate-boring-stuff-scripts')