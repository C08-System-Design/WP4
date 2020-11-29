from D409 import *
from D410 import phi_b, phi_w
import numpy as np
from mat import *
from sympy.solvers import *
from sympy import *

# General constants
alpha_c = A7075_T6.get("alpha")  # thermal coeff lug
alpha_b = Steel.get("alpha")  # thermal coeff fastener
E_b = Steel.get("E")  # Young's mod fastener

# Temp diffs orbit
DT_neg_orbit = 396 - 288.15  # K
DT_pos_orbit = 103 - 288.15  # K
# Temp diffs launch
DT_neg_launch = 298 - 288.15  # K , it is 298 K as discussed in section 8.2
DT_pos_launch = 450 - 288.15  # K

# This is calculated based on D_fi in 4.9, import D_fi !!!
A_sm = (D_fi/2)**2 * np.pi
phi = 0.1  # is different for every configuration

# Function for loads
# alpha_b = fastener, alpha_c = clamped parts


def orbitloads_lug_fast(DT, phi, alpha_c, alpha_b, E_b, A_sm):
    # thermal induced load
    F_T = (alpha_c - alpha_b) * DT * E_b * A_sm * (1-phi)
    return F_T


# Loads for back-plate => phi and alpha for back plate
# (only for pos_launch and neg_orbit --> most relevant)

F_Tpos_back = orbitloads_lug_fast(DT_pos_launch, phi_b, )
F_Tneg_back = orbitloads_lug_fast(DT_neg_launch, phi_b)
F_Tpos_wall = orbitloads_lug_fast()
F_Tneg_wall = orbitloads_lug_fast(DT)

# Loads for vehicle wall => phi and alpha for vehicle wall
# (only for pos_launch and neg_orbit --> most relevant)
# Use lowest Temp for orbit? otherwise there is no DT_neg

"""
Results from this code need to be coupled with all the configs
At this moment, the thermal loads are super small in comparison
to the mechanical in-plane loads
"""
