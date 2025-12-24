# Exercise 62 - Progressive Timed Printer
# Question: Create a program that, once executed the program prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, 4, and so on the interval increases between prints.

from time import sleep
interval = 0

while True :
    print (f'Hello after {interval} seconds')
    sleep(interval)
    interval = interval+1
