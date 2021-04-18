#! python3
# remove_csv_header.py - Removes the header from all CSV files in the cwd.

import csv, os

os.makedirs('header_removed', exist_ok=True)

# Loop through every file in the cwd.
for csv_filename in os.listdir('.'):
  if not csv_filename.endswith('.csv'):
    continue
  
  print('Removing header from ' + csv_filename + '... ')
  # Read the CSV file
  csv_rows = []
  csv_file_obj = open(csv_filename)
  reader_obj = csv.reader(csv_file_obj)
  for row in reader_obj:
    if reader_obj.line_num == 1:
      continue # skip first row
    csv_rows.append(row)
  csv_file_obj.close()
  
  # Write out the CSV file.
  csv_file_obj = open(os.path.join('header_removed', csv_filename), 'w', newline='')
  csv_writer = csv.writer(csv_file_obj)
  for row in csv_rows:
    csv_writer.writerow(row)
  csv_file_obj.close()