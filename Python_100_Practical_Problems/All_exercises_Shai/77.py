# Exercise 77 - Year of Birth Calculator
# Question: Create a script that asks the user to enter their age, and the script calculates the user's year of birth
# and prints it out in a string like in the expected output. Please make sure you generate the current year dynamically.

import datetime as dt
# current_year = int (dt.datetime.now().strftime("%Y"))
current_year = dt.datetime.now().year
print (type(current_year))
print(current_year)

try :
    current_age = int(input("Share your current age : "))
    year_of_birth = current_year - current_age
    print (f"We think you were born in {year_of_birth}")
except Exception as e :
    print ("Incorrect values entered")