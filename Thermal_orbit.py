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

#thermal loads in fastener because of lugs

def orbitloads_lug_fast():
    DT_neg = 103 - 288.15
    DT_pos = 396 - 288.15

    #thermally induced load
    F_Tpos = (alpha_c - alpha_b) * DT_pos * E_b * A_sm * (1-phi)
    F_Tneg =  (alpha_c - alpha_b) * DT_neg * E_b * A_sm * (1-phi)

    return F_Tpos, F_Tneg



#thermal loads in backplate because of vehicle wall
# Assumptions: Looked at this as a cylinder of two materials constrained by two walls (see MoM Problem 4-68)
# (F * t_b)/(A * E_b) + (F * t_w)/(A * E_w) = alpha_b * DT * t_b + alpha_w * DT * t_w
# t = thickness, A = contact surface, E = Young, alpha= thermal expansion coef, DT = difference in temp, _b = backplate, _w = wall



def orbitloads_back_wall():
    F_list_mat = []
    F_list = []
    DT_neg = 103 - 288.15
    DT_pos = 396 - 288.15
    DT_list = [DT_pos, DT_neg]
    F = Symbol("F")
    for mat in mats:
        alpha_b = mat.get("alpha")
        E_b = mat.get("E")
        for DT in DT_list:
            F_minmax = solve((F * t_b) / (A * E_b) + (F * t_w) / (A * E_w) - alpha_b * DT * t_b - alpha_w * DT * t_w, F)
            F_list = F_list + F_minmax

        F_list_mat.append(F_list)
        F_list = []
    return F_list_mat

t_b = 0.002
A = 0.4
E_w = 207 * 10**9
t_w = 0.004
alpha_w = 13.3 * 10**(-6)

print(orbitloads_back_wall())









