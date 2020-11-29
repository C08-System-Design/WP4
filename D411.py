from D410 import *
import numpy as np
from sympy.solvers import *
from sympy import *
from math import pi

# General constants
alpha_c = mat.get("alpha")  # thermal coeff lug
alpha_b = A8090_T8151.get("alpha")  # thermal coeff fastener
E_b = A8090_T8151.get("E")  # Young's mod fastener

# Temp diffs orbit
DT_pos_orbit = 396 - 288.15  # K
DT_neg_orbit = 103 - 288.15  # K
# Temp diffs launch
DT_neg_launch = 298 - 288.15  # K , it is 298 K as discussed in section 8.2
DT_pos_launch = 450 - 288.15  # K

# This is calculated based on D_fi in 4.9, import D_fi !!!
A_sm = (D_fi/2)**2 * np.pi
phi = 0.1  # is different for every configuration

# Function for loads
# alpha_b = fastener, alpha_c = clamped parts


def loads_lug_fast(DT, phi, alpha_c, alpha_b, E_b, A_sm):
    # thermal induced load
    F_T = (alpha_c - alpha_b) * DT * E_b*1e9 * A_sm * (1-phi)

    return F_T


# print("Proposed effective stiffness area", D_fi*t)
# print(configs[0][2])
# print(phi_b[0])
# print("Current stiffness area", D_fi**2/4*pi)
# Loads for back-plate => phi and alpha for back plate
# (only for pos_launch and neg_orbit --> most relevant)
t = t2+t3  # backplate + wall thickness


def get_thermal_loads(mat, i):
    F_Tpos_bl = loads_lug_fast(
        DT_pos_launch, phi_b[i], mat.get("alpha"), alpha_b, E_b, configs[i][2]**2/4*pi)
    F_Tpos_bo = loads_lug_fast(
        DT_pos_orbit, phi_b[i], mat.get("alpha"), alpha_b, E_b, configs[i][2]**2/4*pi)
    F_Tneg_bl = loads_lug_fast(
        DT_neg_launch, phi_b[i], mat.get("alpha"), alpha_b, E_b, configs[i][2]**2/4*pi)
    F_Tneg_bo = loads_lug_fast(
        DT_neg_orbit, phi_b[i], mat.get("alpha"), alpha_b, E_b, configs[i][2]**2/4*pi)
    F_Tpos_wl = loads_lug_fast(
        DT_pos_launch, phi_w[i], mat.get("alpha"), alpha_b, E_b, configs[i][2]**2/4*pi)
    F_Tpos_wo = loads_lug_fast(
        DT_pos_orbit, phi_w[i], mat.get("alpha"), alpha_b, E_b, configs[i][2]**2/4*pi)
    F_Tneg_wl = loads_lug_fast(
        DT_neg_launch, phi_w[i], mat.get("alpha"), alpha_b, E_b, configs[i][2]**2/4*pi)
    F_Tneg_wo = loads_lug_fast(
        DT_neg_orbit, phi_w[i], mat.get("alpha"), alpha_b, E_b, configs[i][2]**2/4*pi)
    return [F_Tpos_bl, F_Tpos_bo, F_Tneg_bl, F_Tneg_bo,
            F_Tpos_wl, F_Tpos_wo, F_Tneg_wl, F_Tneg_wo]


maxTLs = []
minTLs = []
for i in range(18):
    maxTL = max(get_thermal_loads(mat, i))  # max thermal load
    minTL = min(get_thermal_loads(mat, i))  # min thermal load
    maxTLs.append(maxTL)
    minTLs.append(minTL)
    ML = loads_mag[i]  # mechanical load, is already max
    # print(get_thermal_loads(mat, i))
    # print(configs[i][2], "[m]")
# Loads for vehicle wall => phi and alpha for vehicle wall
# (only for pos_launch and neg_orbit --> most relevant)
# Use lowest Temp for orbit? otherwise there is no DT_neg
