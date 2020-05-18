import re

def scraper(text):

    contacts = []

    emailRegex = re.compile(r'\S+@\S+')

    extEmail = emailRegex.findall(text)

    phoneRegex = re.compile(r'''
    (
    (\+\d{2})?          #+91(int'l-code)
    (\s|-|\()?           #1st separator
    ((\d{2,3})?)?         #area code
    (\s|-|\))?               #2nd separator
    \d{8,10}              #Actual Digits
    )
    ''',re.VERBOSE)

    extPhone = phoneRegex.findall(text)

    int={'email':extEmail,'phone':extPhone} # Assumes every email has a phone number attached.
    for i in range(len(int['phone'])):
        int2=int['phone'][i][0] +' '+ int['email'][i]
        contacts.append(int2)

    return contacts
print('Enter the content which contains emails and phone numbers')

var = input()

appendedContacts = scraper(var)

print(appendedContacts)
