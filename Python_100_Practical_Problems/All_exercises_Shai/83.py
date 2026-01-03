# Question: Write a script that detects and prints out your monitor resolution.

import screeninfo as si

print (si.get_monitors()[0])
print (type(si.get_monitors()[0]))

print (si.get_monitors()[0].width)
# print (type(si.get_monitors()[0]))
print (si.get_monitors()[0].height)
print (f'Width : {si.get_monitors()[0].width}, Height : {si.get_monitors()[0].height}')