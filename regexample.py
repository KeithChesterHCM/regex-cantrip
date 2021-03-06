# regexample.py
import sys,re

phone_pattern = re.compile(r'^(1-)?[0-9]{3}-[0-9]{3}-[0-9]{4}$')
email_pattern = re.compile(r'^[a-zA-Z0-9.\-_]+@[a-zA-Z0-9.\-_]+\.[a-zA-Z]{2,4}$')
date_pattern = re.compile(r'^[0-9]{1,2}(-|/)[0-9]{1,2}(-|/)[0-9]{1,4}$')
zip_pattern = re.compile(r'^[0-9]{5}$')
ssn_pattern = re.compile(r'^[0-9]{3}-[0-9]{2}-[0-9]{4}$')

print 'What type of information would you like to validate?'
print '1) Phone number'
print '2) Email address'
print '3) Date'
print '4) Zip code'
print '5) SSN'
print '6) Quit'
choice = raw_input('>> ')

while re.match(r'^[1-6]$',choice) == None:
  print 'Bad input.'
  choice = raw_input('>> ')

if choice == '1':
  msg = 'Enter a phone number: '
  p = phone_pattern
elif choice == '2':
  msg = 'Enter an email address: '
  p = email_pattern
elif choice == '3':
  msg = 'Enter a date: '
  p = date_pattern
elif choice == '4':
  msg = 'Enter a zip coe: '
  p = zip_pattern
elif choice == '5':
  msg = 'Enter a SSN: '
  p = ssn_pattern
elif choice == '6': sys.exit(0)

user_input = raw_input(msg)

while p.match(user_input) == None:
  print 'Bad input.'
  user_input = raw_input(msg)

print 'Success! You entered: ' + user_input
