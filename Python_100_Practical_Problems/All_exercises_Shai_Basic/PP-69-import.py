import importlib

module_name = "PP-62-Class"
my_module = importlib.import_module(module_name)


# import PP-62-Class
# from PP-62-Class import Car

new_gaadi = my_module.Car(2024, "Mercedes" ,"Sexy")
print (f" Bought in year {new_gaadi.year}, my {new_gaadi.make} is {new_gaadi.model} with age {new_gaadi.age()}")