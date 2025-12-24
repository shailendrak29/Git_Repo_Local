# Exercise 63 - Progressive Time Printer with Threshold
# Question: Create a program that, once executed the programs prints Hello  instantly first, then it prints it after 1 second, then after 2, 3,
# and then the program prints out the message "End of the Loop" and stops.

from time import sleep

interval = 1

while (interval <4) :
    sleep(interval)
    print(f'Hello after {interval} seconds')
    interval = interval + 1

print ('End of the Loop')