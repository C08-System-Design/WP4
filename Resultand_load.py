from math import *
from sympy import *
from Thermal_orbit import Loads_therm
from launch_loads import F_x

# F_x is also F_y so I'm converting it for clarity
F_y = F_x
# Calculating the resulting force due to thermal stresses and lateral stresses

F_yres = F_y + Loads_therm[0][0]
print(F_yres)