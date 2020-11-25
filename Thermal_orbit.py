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
    DT_plus = 103 - 288.15
    DT_min = 396 - 288.15

    #thermally induced load
    F_Tplus = (alpha_c - alpha_b) * DT_plus * E_b * A_sm * (1-phi)
    F_Tmin =  (alpha_c - alpha_b) * DT_min * E_b * A_sm * (1-phi)

    return F_Tplus, F_Tmin



#thermal loads in backplate because of vehicle wall
# Assumptions: Looked at this as a cylinder of two materials constrained by two walls (see MoM Problem 4-68)
# (F * t_2)/(A * E_b) + (F * t_w)/(A * E_w) = alpha_b * DT * t_2 + alpha_w * DT * t_w

def orbitloads_back_wall():






    return
