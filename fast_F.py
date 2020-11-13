"""
Determine net force F_cg acting at cg calculated in fast_cg.py
It is composed of F_cgx and F_cgz
Both must be parallel to F_x and F_z and the same in magnitude
There might be a moment arm d creating M_cgy
F_x = F_in-plane-x, F_z = F_in-plane-z and F_M_y = F_in-plane-M_y
    These are contributions of a SINGLE fastener
n_f is the number of fasteners
F_cg is a vector sum of loads F_x and F_z determined previously
"""

from math import sqrt


def get_F_cg(F_x, F_z):
    F_cg = sqrt(F_x**2+F_z**2)
    return F_cg


def get_F_x(F):  # F = F_cgx 
    n = A_i.__len__()  # number of fasteners
    F_x = F/n
    return F_x


def get_F_z(F):  # F = F_cgz 
    n = A_i.__len__()  # number of fasteners
    F_z = F/n
    return F_z


def get_F_M_y(M, A, r):  # M is moment, A is fastener area and r is fastener arm
    F_M_y = M*sum(A)*sum(r)/sum(A)/sum(r)/sum(r)
    return F_M_y


def get_r_i(x, z):
    r = sqrt(x**2+z**2)
    return r


# decompose F_cg into F_cgx and F_cgz
A_i = []
x_i = []
z_i = []
r_i = []  # radial distances of fasteners to fast_cg, from Luke or calculate?
for i in range(A_i.__len__()):
    r_i.append(get_r_i((x_i[i], z_i[i])))

get_F_x()
get_F_z()
get_F_M_y()
