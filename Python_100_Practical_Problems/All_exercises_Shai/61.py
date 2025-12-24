# Exercise 61 - Timed Printer
# Question: Create a program that prints out Hello  every two seconds.

import time
i=0

while True :
    print (f'Tik tik {i}')
    time.sleep(1)
    i=i+1