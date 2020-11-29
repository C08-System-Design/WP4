from D409 import *
from mat import *
import numpy as np


def forceratio(E_a, E_b, t, D_fo, D_fi):
    
    # input = Young's mod of material for attach, Young's mod of mat for fast,
    # variables for compliance of attachment mechanism
    # these are D_fo and D_fi inputted to this function
    """Calc of attachment compliance"""
    da = 4*t / (E_a*np.pi*(D_fo**2 - D_fi**2))

    # Variables for Compliance of fastener

    d = D_fi  # diameter of shank
    A_sha = np.pi * (d/2)**2  # cross-section area of shank
    L_sha = t2+t3  # length of shank is both plate thicknesses combined
    # imported from push_fail.py, they are constant at the moment
    A_nom = np.pi * D_fo**2  # nominal cross-section area
    A_3 = A_sha  # area for engaged shank

    '''Calc of fastener compliance'''
    L_hsub = 0.5*d
    L_engsub = 0.4*d
    L_nsub = 0.4*d

    db = 1/E_b * (L_hsub/A_nom + L_engsub/A_3 + L_sha/A_sha)\
        + L_nsub/(E_b * A_nom)

    phi = da/(da+db)  # Force ratio
    return phi


# thickness is taken from push_fail, assumed constant
t_b = t2  # from D409
t_w = t3  # from D409

# to asses force ratio of wall thickness
phi_w = []  # force ratios for wall of every configuration
for config in configs:
    D_fo = config[2]+config[2]*0.4  # same as in push_fail.py, 0.4 is arbitrary
    D_fi = config[2]
    phi = forceratio(A2195_T84.get("E"), Steel.get("E"), t_w, D_fo, D_fi)
    phi_w.append(phi)

# to asses force ratio of backplate thickness
phi_b = []  # force ratios for backplate of every configuration
for config in configs:
    D_fo = config[2]+config[2]*0.4  # same as in push_fail.py, 0.4 is arbitrary
    D_fi = config[2]
    phi = forceratio(A7075_T6.get("E"), Steel.get("E"), t_b, D_fo, D_fi)
    phi_b.append(phi)
