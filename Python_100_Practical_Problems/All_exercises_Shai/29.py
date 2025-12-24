# Question:  Please write a function that calculates liquid volume in a sphere using the following formula. The radius r  is always 10, so consider making it a default parameter.
# You can then test your solution by passing 2 for h and you should get the expected output.
# Expected output: 4071.5040790523717

import numpy as np
print (np.pi)

# r = 10
# h = 2

def sphere_vol(h,r=10):
    vol = ((4*np.pi*r**3)/3)-((np.pi*h**2*((3*r)-h))/3)
    print (vol)

sphere_vol(2)

def sphere_vol(h,r=10) # works
def sphere_vol(r=10,h) #SyntaxError: non-default argument follows default argument