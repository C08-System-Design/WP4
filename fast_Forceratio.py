"""
Force ratio calculation
"""
from push_fail import *
from mat import *
import numpy as np


def forceratio(E_a, E_b, t, D_fo, D_fi):
    
    # input = Young's mod of material for attach, Young's mod of mat for fast,
    # variables for compliance of attachment mechanism
    # these are D_fo and D_fi inputted to this function
    """Calc of attachment compliance"""
    da = 4*t / (E_a*np.pi*(D_fo**2 - D_fi**2))

    # Variables for Compliance of fastener

    d = D_fo  # diameter of head/nut
    A_sha = np.pi * (d/2)**2  # cross-section area of shank
    L_sha = t2+t3  # length of shank is both plate thicknesses combined
    # imported from push_fail.py, they are constant at the moment
    A_nom = A_sha  # nominal cross-section area
    A_3 = A_sha  # area for engaged shank

    '''Calc of fastener compliance'''
    L_hsub = 0.5*d
    L_engsub = 0.4*d
    L_nsub = 0.4*d

    db = 1/E_b * (L_hsub/A_nom + L_engsub/A_3 + L_sha/A_sha)\
        + L_nsub/(E_b * A_nom)

    phi = da / (da+db)  # Force ratio
    return phi


for config in configs:
    forceratio(1, 2, 3, 4, 5)
    print("testing")

# forceratio(E_a, E_b, t_w)  # to asses force ratio of wall thickness
# forceratio(E_a, E_b, t_b)  # to asses force ratio of backplate thickness
