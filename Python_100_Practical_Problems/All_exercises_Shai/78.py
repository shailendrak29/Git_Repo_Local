# create random password 6 random alphanumeric character in the range

import string as s, random as r

print (s.ascii_lowercase)
print (s.ascii_uppercase)
print (s.digits)
print (s.punctuation)
created_passwords =[]
valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*?@^'
print (valid_chars)

# print ("".join(r.sample(valid_chars, 6)))
# print ("|".join(r.sample(valid_chars, 6)))

chosen_chars = r.sample(valid_chars,6)
password = "".join(chosen_chars)
print (password)
# created_passwords.append(password)
# print (created_passwords)

if (password not in created_passwords) :
    created_passwords.append(password)
    print (created_passwords)
else :
    print ("Already present.. tried again ")

# wanted to create somthing that compels the code to find a unique password, that was not created before
