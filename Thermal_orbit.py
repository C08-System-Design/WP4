""" In orbit thermal loads """
import numpy as np
import mat as mat

#General constants
alpha_c = #thermal coeff lug
alpha_b = #thermal coeff fastener
E_b = #young's mod fastener
A_sm = #stiffness area of fastener
phi =#force ratio

#thermal loads in fastener because of lugs

def orbitloads_lug_fast():
    DT_plus = 288.15 - 103
    DT_min = 288.15 - 396

    #thermally induced load
    F_Tplus = (alpha_c - alpha_b) * DT_plus * E_b * A_sm * (1-phi)
    F_Tmin =  (alpha_c - alpha_b) * DT_min * E_b * A_sm * (1-phi)

    return F_Tplus, F_Tmin



#thermal loads in backplate because of vehicle wall

def orbitloads_back_wall():






    return
