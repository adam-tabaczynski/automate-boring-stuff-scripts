#! python3
# read_census_excel.py - Tabulates population and number of census tracts for
# each county.

import openpyxl
import pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('./automate_online-materials/censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
  # Each row in the spreadsheet has data for one census tract.
  state = sheet['B' + str(row)].value
  county = sheet['C' + str(row)].value
  pop = sheet['D' + str(row)].value
  
  # Make sure the key for this state exists.
  county_data.setdefault(state, {})
  
  # Make sure the key for this county in this state exists.
  county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})
  
  # Each row represents one census tract, so increment by one.
  county_data[state][county]['tracts'] += 1
  
  # Increase the county population by the pop value in the census tract.
  county_data[state][county]['pop'] += int(pop)
  
# Open a new text file and write the contents of county_data to it.
print('Writing results...')
result_file = open('./chapter_13/census2010.py', 'w')
result_file.write('all_data = ' + pprint.pformat(county_data))
result_file.close()
print('Done.')