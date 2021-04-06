# dateDetection.py - program that checks if given date is valid.
# 04, 06, 09, 11 - 30days
# 01, 03, 05, 07, 08, 10, 12 - 31days
# 02 - 28 days
# If year is divisible by 4, then 02 is 29 days, 28 days if divisble by 100, and 29 if divisible by 400.

import re, sys


def date_validation_program():
    validDateRegex = re.compile(r'''(
        ( 0[1-9] | 1[0-9] | 2[0-9] | 3[0-1] ) # day check
        / # separator
        ( 0[1-9] | 1[0-2] ) # month check
        / # separator
        ( [1-2][0-9][0-9][0-9] ) # year check (from 1000 to 2999)
    )''', re.VERBOSE)
    
    print('You are in date validation program for years 1000 - 2999')
    while True:
        userDate = None
        while userDate == None:    
            userDate = get_user_date(validDateRegex)

        validate_date(userDate)
    

def get_user_date(dateRegex):
    print('Please type in date to check if its valid:')
    print('proper format: DD/MM/YYYY')
    userDate = input()
    try:       
        matchingDateObject = dateRegex.search(userDate)
        print('You typed in: ' + matchingDateObject.group() + '\n')
        return userDate
    except AttributeError:
        print('\nEither you typed in invalid date (ex. 33/13/3000), date that exceed given \
               year span (1000-2999) or not used proper format DD/MM/YYYY.\n')
    

def validate_date(userDate):
    
    day, month, year = userDate.split('/')

    isLoopYear = loop_year_check(year)
    isDateWrong, errorMessage = validate_month_and_day(day, month, isLoopYear)

    if isDateWrong:
        print(errorMessage)

    else:
        print(f'Parsed value {uInput} is valid.')

    exit_banner()


def loop_year_check(year):
    if int(year) % 4 == 0:
        return True
    elif int(year) % 100 == 0 and int(year) % 400 == 0:
        return True
    else:
        return False

def validate_month_and_day(day, month, isLoopYear):
    months_with_30days = ['04', '06', '09', '11']
     = ['01', '03', '05', '07', '08', '10', '12']
    
    if month in months_with_30days:
        if int(day) < 1 or int(day) > 30:
            return (True, f'Error with parsed day: {day}. It should have value between 01 and 30.')

    elif month in months_with_31days:
        if int(day) < 1 or int(day) > 31:
            return (True, f'Error with parsed day: {day}. It should have value between 01 and 30.')

    else:
        if(isLoopYear):
            if int(day) < 1 or int(day) > 29:
                return (True, f'Error with parsed day: {day}. It should have value between 01 and 29.')
        else:
            if int(day) < 1 or int(day) > 28:
                return (True, f'Error with parsed day: {day}. It should have value between 01 and 28.')
            
    return (False, '')


def exit_banner():
    print("Want to check another date? Type in 'n' to exit program or anything else to continue.")
    user_input = input()
    if user_input == 'n':
        sys.exit()
            
date_validation_program()
