from math import sqrt
from sympy import *
from Thermal_orbit import *
from fast_loads import *
from fast_Forceratio import phi_b, phi_w

# Calculating the resulting force due to thermal stresses and lateral stresses
# phi is NOT a real value I think. It's dependant on if the fastener is eccentric or concentric and we didn't research that.
#currently done for A7075_Y6
#F_Tpos_back, F_Tneg_back = orbitloads_lug_fast(DT_pos_launch, DT_neg_launch, 0.5, 22.0*10**(-6), 11.3*10**(-6), 207*10**9., A_sm)


# It is assumed that the in plane mechanical forces act in the same direction as the thermal stresses so that it gives a
# conservative answer.
def resultant_load():
    F_res_pos_back = sqrt(F_xi**2 + F_zi**2) + F_Tpos_back
    F_res_neg_back = sqrt(F_xi**2 + F_zi**2) + F_Tneg_back
    F_res_pos_wall = sqrt(F_xi**2 + F_zi**2) + F_Tpos_wall
    F_res_neg_wall = sqrt(F_xi**2 + F_zi**2) + F_Tneg_wall
    return F_res_pos_back, F_Tneg_back, F_res_pos_wall, F_res_neg_wall

# Calculate bearing stress for these new vlues
