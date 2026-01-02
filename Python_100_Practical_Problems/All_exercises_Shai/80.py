# create a script to validate 3 password conditions :
# 1.Password contains at least one number
# 2. Contains one uppercase letter
# 3. Atleast 5 chars long
# print out "Password is not fine" if the user did n't create a correct password

import string as s
import re


while True :
    error_msg = ''+'\n'
    password = input ("Enter the password : ")

    if (len(password) <= 4) :
        error_msg = error_msg+'Need atleast 5 characters'+'\n'

    if (not any( i.isdigit() for i in password )) :
        error_msg = error_msg+'Need atleast one number'+'\n'

    if (not any( i.isupper() for i in password)) :
        error_msg = error_msg+'Need atleast one uppoer case character'+'\n'

    if (len(password) > 4 and any( i.isdigit() for i in password ) and any( i.isupper() for i in password) ) :
        print ("Valid password")
        break
    else :
        print ("Password is not fine")
        print (f'Error message : {error_msg}')