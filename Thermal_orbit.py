""" In orbit thermal loads """
import numpy as np
from mat import *
from sympy.solvers import *
from sympy import *

#General constants
# alpha_c = #thermal coeff lug
# alpha_b = #thermal coeff fastener
# E_b = #young's mod fastener
# A_sm = #stiffness area of fastener
# phi =#force ratio
# DT = temperature difference

#Temp diffs

DT_neg_orbit = 396 - 288.15 #K
DT_pos_orbit = 103 - 288.15 #K

DT_neg_launch = XXX - 288.15 #K #What temperature do we consider here? still not clear to me => discuss
DT_pos_launch = 450 - 288.15 #K


#This is calculated based on D_fi in 4.9, import D_fi !!!
A_sm = (D_fi/2)**2 * np.pi



#Function for loads

def orbitloads_lug_fast(DT_pos, DT_neg, phi, alpha_c, alpha_b, E_b, A_sm):
    
    #thermal induced load
    
    F_Tpos = (alpha_c - alpha_b) * DT_pos * E_b * A_sm * (1-phi)
    F_Tneg =  (alpha_c - alpha_b) * DT_neg * E_b * A_sm * (1-phi)

    return F_Tpos, F_Tneg



# Loads for back-plate => phi and alpha for back plate (only for launch --> most relevant)

F_Tpos_back, F_Tneg_back = orbitloads_lug_fast(DT_pos_launch, DT_neg_orbit, phi, alpha_c, alpha_b, E_b, A_sm)


# Loads for vehicle wall => phi and alpha for vehicle wall (only for launch --> most relevant)
# Use lowest Temp for orbit? otherwise there is no DT_neg

F_Tpos_wall, F_Tneg_wall = orbitloads_lug_fast(DT_pos, DT_neg, phi, alpha_c, alpha_b, E_b, A_sm)


"""
Results from this code need to be coupled with all the configs
At this moment, the thermal loads are super small in comparison
to the mechanical in-plane loads
"""
