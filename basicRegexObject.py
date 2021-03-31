import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # raw string is required.
mo = phoneNumRegex.search('My number is 415-555-4242.')

print('Phone number found: ' + mo.group()) # returns None if nothing matched.

phoneNumGroupsRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # parentheses allow using .group()
mo1 = phoneNumGroupsRegex.search('My number is 415-555-4242.')

print(mo1.group(1))
print(mo1.group(2))
print(mo1.group(0))
print(mo1.group()) # no index and zero index points to the whole matched string.


heroRegex = re.compile(r'Batman|Tina Fey')
mo2 = heroRegex.search(' and Tina Fey')
print(mo2.group())

mo3 = heroRegex.search('Tina Fey and Batman')
print(mo3.group())


dotsRegex = re.compile(r'\s|-\.?')
mo4 = dotsRegex.findall("---")
print(mo4)
