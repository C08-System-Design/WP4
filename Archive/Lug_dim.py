#from mat import A2195_T84
from launch_loads import long_force, lat_force
import math
#constants

clearance = 0.08 # * 39.3701
sigma_y = 490 * 10**6 # space aluminium
x0 = 0.0848 # * 39.3701 # from overleaf

# guess
a = 0.02 # * 39.3701
t = 0.005 # * 39.3701
ktu = 0.9


total_force = math.sqrt(long_force**2+lat_force**2)*1.5 # 1.5 = safety factor
r = math.sqrt((0.5*total_force / sigma_y * math.pi))
# r = r * 39.3701
# print(r*2)

A = long_force/(sigma_y * ktu)
# A = A * 1550

# print(A)
# print(D)

# Moment around x
Mx_stress = 0.5 * (long_force*clearance*0.5*a)/((1/12)*(t)*a**3)
# print(Mx_stress)

# Moment around z
Mz_stress = (lat_force*clearance*((x0*0.5)+(t)))/(2*((1/12)*a*(t)**3+a*(t)*(0.5*x0+0.5*t)**2))
# print(Mz_stress)

# lateral load stress
lat_stress = 0.5 * (lat_force/((t) * a))
# print(lat_stress)

total_stress = Mx_stress + Mz_stress + lat_stress
print(total_stress)

print(r)
print(a)
t = (1.875*(0.5*a - r)*(a - 1.41421*r))/(r*(3*a-5.41421*r))
print(t)

D = A/t
# Geometric properties
# A1 = 0.5 * a - 0.5*math.sqrt(2)*r

# A2 = 0.5*a - r

# A3 = A2
# A4 = A1

# Aav = (6)/((3/A1)+(1/A2)+(1/A3)+(1/A4))
Abr = 2*r * t
Dt = (long_force * 1.5) / (0.9 * sigma_y) 
print(Dt * 10**6)

# print(Aav/Abr)
# Bending stress
# moment = clearance * long_force
# print(moment)
# width = ((60*moment)/sigma_y)**(1/3)
# print(width)

# Detailed design

# Kbry is dependent on t/D and e/D
# t/D


# Pbry = Kbry * Fty * Abr