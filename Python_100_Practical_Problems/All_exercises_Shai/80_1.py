# create a script to validate 3 password conditions :
# 1.Password contains at least one number
# 2. Contains one uppercase letter
# 3. Atleast 5 chars long
# print out "Password is not fine" if the user did n't create a correct password
#using list

import string as s
import re

while True :
    error_msg = []
    password = input ("Enter the password : ")

    if (len(password) <= 4) :
        error_msg.append('Need atleast 5 characters')

    if (not any( i.isdigit() for i in password )) :
        error_msg.append('Need atleast one number')

    if (not any( i.isupper() for i in password)) :
        error_msg.append('Need atleast one uppoer case character')

#     print (len(error_msg))

    if (len(error_msg)==0 ) :
        print ("Valid password")
        break
    else :
        print ("Password is not fine")
#         print (f'Error message : {error_msg}')
        for msg in error_msg :
            print (msg)