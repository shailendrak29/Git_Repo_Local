# Question: Please take a look at the following list:
#
# checklist = ["Portugal", "Germany", "Munster", "Spain"]
#
# One of the items is not a country. Please use Python and the file containing the list of countries (attached) as the data source to filter out the checklist  of non-country items. Once you have filtered out checklist , then print it out.

checklist = ["Portugal", "Germany", "Munster", "Spain"]
# print (checklist)
valid_countries = []

with open("countries_clean_1.txt","r") as f :
    valid_countries = f.readlines()

# print (valid_countries)
valid_countries_1 = [ item.strip('\n') for item in valid_countries]
# print (valid_countries_1)

checklist =[ check for check in checklist if check in valid_countries_1 ]
print (checklist)
