# Question: Please download the attached countries-raw.txt file. The file contains the list of country names, but it also contains some unnecessary text among the countries.
# Please clean the list with Python by generating a new text file that contains a flawless list of country names without any other text or brake lines in it. The new file content should look like in the expected output.

#
# import pycountry
# countries_list = []
countries_raw =[]
countries_raw1 =[]
#
# for country in pycountry.countries:
#     countries_list.append(country.name)
#     print(country.name)
#
# print (countries_list.sort())
# print (countries_list[1])

with open ("countries_raw.txt", "r") as f :
#     countries_raw1.append(f.readlines())
    countries_raw = f.readlines()

# countries_cleaned = [item.strip('\n') for item in countries_raw if (len(item)> 1) and item != '\n' ]
countries_cleaned = [item for item in countries_raw if (len(item.strip('\n'))> 1) and item != '\n' and item.strip('\n') != 'Top of Page' ]

print (countries_cleaned)
print (len(countries_cleaned))

with open ("countries_clean.txt", "w") as f :
    for item in countries_cleaned :
        f.write(item)