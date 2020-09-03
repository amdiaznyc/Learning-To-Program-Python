#############
#Module:  address-book.py
#Author:  A.M.D
#Version: Draft
'''
This program provides a simple address book.
'''
##############
#Log
#09/03/2020  --file created
#
#############
# address book using a List
addressBook = [
['Fred', '9 Some St', 'Anytown', '0123456789'],
['Rose', '11 Nother St', 'SomePlace', '0987654321']
]



# address book using a Dictionary or Hash
addressBook = {
'Fred' : ['Fred', '9 Some St', 'Anytown', '0123456789'],
'Rose' : ['Rose', '11 Nother St', 'SomePlace', '0987654321']
}

# another example of address book consisting of a dictionary whose keys are the names and the values are dictionaries whose keys are the field names
addressBook = {
    'Fred' : {'name':    'Fred',
              'street':  '9 Some St',
              'town':    'Anytown',
              'tel':     '0123456789'},
    'Rose' : {'name':    'Rose',
              'street':  '11 Nother St',
              'town':    'SomePlace',
              'tel':     '0987654321'}
    }

   
