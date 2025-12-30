# create a script to validate 3 password conditions :
# 1.Password contains at least one number
# 2. Contains one uppercase letter
# 3. Atleast 5 chars long
# print out "Password is not fine" if the user did n't create a correct password

import string as s
import re

# password = input ("Enter the password : ")
# print (s.ascii_lowercase)
# print (s.ascii_uppercase)
# print (s.digits)

# length_password = len(password)
# print (len(password))

# if ( (len(password) > 4 ) and re.search('[0-9]', password) and re.search('[A-Z]', password)) :
#     print ("Valid password")
# else :
#     print ("Password is not fine")
#

# if re.search('[0-9]', password)  :
#     print ("Valid password")
# else :
#     print ("Password is not fine")

while True :
    password = input ("Enter the password : ")
    if (len(password) > 4 and any( i.isdigit() for i in password ) and any( i.isupper() for i in password) ) :
        print ("Valid password")
        break
    else :
        print ("Password is not fine")