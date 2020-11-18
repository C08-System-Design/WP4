#from mat import A2195_T84
from launch_loads import long_force, lat_force
import math
#constants

clearance = 0.08
sigma_y = 490 * 10**6  # space aluminium
t = 0.0005

# guess
a = 2*0.02370675
t = 0.5 * a
x0 = 0.0848 #from overleaf


A = long_force/(sigma_y * 2)
D = A/t
print(A)
print(D)

# Moment around x
# Mx_stress = 0.5 * (long_force*clearance*0.5*a)/((1/12)*(t)*a**3)
# print(Mx_stress)

# Moment around z
# Mz_stress = (lat_force*clearance*((x0*0.5)+(t)))/(2*((1/12)*a*(t)**3+a*(t)*(0.5*x0+0.5*t)**2))
# print(Mz_stress)

# lateral load stress
# lat_stress = 0.5 * (lat_force/((t) * a))
# print(lat_stress)

# total_stress = Mx_stress + Mz_stress + lat_stress
# print(490 * 10**6 - total_stress)

# Geometric properties
diameter = a
A1 = 0.5*(diameter)-0.5*(diameter)*0.5*2**0.5+2*t
# A1 = 0.5 * a -1/4 * 2**0.5 * a -0.5 * 2**0.5 * t

# A2 = a - diameter
A2 = t

A3 = A2
A4 = A1

Aav = (6)/((3/A1)+(1/A2)+(1/A3)+(1/A4))
Abr = diameter * t

print(Aav/Abr)
# Bending stress
# moment = clearance * long_force
# print(moment)
# width = ((60*moment)/sigma_y)**(1/3)
# print(width)

# Detailed design

# Kbry is dependent on t/D and e/D
# t/D


# Pbry = Kbry * Fty * Abr