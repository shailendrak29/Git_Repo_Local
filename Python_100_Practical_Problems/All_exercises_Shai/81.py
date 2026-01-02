# create a script to validate 3 password conditions :
# 1.Password contains at least one number
# 2. Contains one uppercase letter
# 3. Atleast 5 chars long
# print out "Password is not fine" if the user did n't create a correct password
#using list
# before password ask for username. make sure it new

import string as s
import re

# Accept username
x=0
credentials = {}

while True :
    user_check = []
    users_list = []
    username =input ("Enter user name : ")

    with open ("users.txt","r") as f :
        raw_users_list = f.readlines()
#         users_list.append(f.read())

    users_list = [item.strip('\n') for item in raw_users_list]

    print (users_list)
    print (username)
    if (username in users_list) :
        print ("Exisiting User")
    else :
        print ("New username")
        with open ("users.txt","a") as f :
            f.write(username+'\n')
        break

# Accept password
while True :
    error_msg = []
    password = input ("Enter the password : ")

    if (len(password) <= 4) :
        error_msg.append('Need atleast 5 characters')

    if (not any( i.isdigit() for i in password )) :
        error_msg.append('Need atleast one number')

    if (not any( i.isupper() for i in password)) :
        error_msg.append('Need atleast one uppoer case character')

    if (len(error_msg)==0 ) :
        print ("Valid password")
        break
    else :
        print ("Password is not fine")
        for msg in error_msg :
            print (msg)

credentials = {"username" : username,"password" : password}
print (credentials)
print (str(credentials))

with open ("credentials.txt","a") as f :
     f.write(str(credentials)+'\n')