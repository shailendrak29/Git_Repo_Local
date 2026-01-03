# Question: Use Python to calculate the distance in kilometers between Jupiter and Sun on January 1, 1230.

import ephem as ep

jupiter = ep.Jupiter()

print (jupiter)
# jupiter.compute()
date_to_compute = '1230/01/01'
jupiter.compute(date_to_compute)
print (jupiter.earth_distance)
print (jupiter.sun_distance * 149597870.691)

# 758085657.5026425
# 758085657.5026425
