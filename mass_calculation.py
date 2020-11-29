import numpy as np
from D413 import *

'''Mass Calculation'''

# This document gives the formulas for the mass calculation, but haven't fixed input
# It needs all the dimensions of the attachment system


'''Calculate total Volume'''

V_1 = (w_1 * (D_1 / 2) - ((np.pi * (D_1 / 2)**2 ) / 2) )* t_1 + ((np.pi * (w_1 / 2)**2)/2 - ((np.pi * (D_1 / 2)**2)/2 )) * t_1
V_2 = w_1 * t_1 * (l * (D_1 / 2))

#n is the total number of holes in back-plate
V_3 = (w_1 * w_2 - n * np.pi * (D_2 / 2)**2 ) * t_2

V = V_1 + V_2 + V_3

mass = mat.get("rho") * V

print("The final estimated mass is", mass, "kg")

