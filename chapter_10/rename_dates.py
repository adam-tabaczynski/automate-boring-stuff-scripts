#! python3
# rename_dates.py - Renames filenames w/ American MM-DD-YYYY date format
# to European DD-MM-YYYY format.

import shutil, os, re

# Create a regex that matches file with the American date format.
date_pattern = re.compile(r"""^(.*?) # all text before the date
                         ((0|1)?\d)- # one or two digits for the month
                         ((0|1|2|3)?\d)- # one or two digits for the day
                         ((19|20)\d\d) # four digits for the year
                         (.*?)$ # all text after the date
                         """, re.VERBOSE)

# TODO: Loop over the files in the working directory.
for american_filename in os.listdir('.//chapter_10//american_to_european_dates'):
  mo = date_pattern.search(american_filename)
  
  # Skip files w/o a date.
  if mo == None:
    continue
  
  # Get the different parts of the filename.
  before_part = mo.group(1)
  month_part = mo.group(2)
  day_part = mo.group(4)
  year_part = mo.group(6)
  after_part = mo.group(8)
  
  # Form the European-style filename.
  european_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part
  
  # Get the full, absolute file paths.
  absolute_working_dir = os.path.abspath('.//chapter_10//american_to_european_dates')
  american_filename = os.path.join(absolute_working_dir, american_filename)
  european_filename = os.path.join(absolute_working_dir, european_filename)
  
  # Rename the files.
  #print(f'Renaming\n"{american_filename}"\n\t\tto\n"{european_filename}"...\n')
  
  shutil.move(american_filename, european_filename) # uncomment after testing