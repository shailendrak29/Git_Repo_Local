pwr=0
i = 0

while (pwr<100):   #1000000000
    i+=1
    pwr = 2**i
    print ("{} is value for {}".format(pwr,i))

print ("2 raised to {} power, is greater than 1,000,000,000".format(i))