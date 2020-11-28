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

from math import sqrt, pi
from launch_loads import *  # retrieve loads
from pattern import configs, D


def get_F_cg(Fx, Fz):
    F_cg = sqrt(Fx**2+Fz**2)
    return F_cg


def get_F_x(F):  # F = F_cgx 
    n = A_i.__len__()  # number of fasteners
    Fx = F/n
    return Fx


def get_F_z(F):  # F = F_cgz 
    n = A_i.__len__()  # number of fasteners
    Fz = F/n
    return Fz


def get_F_M_y(M, A, r, Ai, ri):  # M is moment, A is A_f, Ai and ri are lists
    # with all fasteners and r is fastener arm
    F_M_y = M*A*r/sum(Ai)/sum(ri)/sum(ri)
    return F_M_y


def get_r_i(x, z):
    r = sqrt(x**2+z**2)
    return r


# there will not be any moment as everything is symmetric
configs_loads = []
loads = []
for config in configs:
    # retrieve fastener data
    x_i = config[0]
    z_i = config[1]
    A_i = []
    for i in range(len(x_i)):
        A_i.append(pi*D**2/4)

    # calculate
    r_i = []  # radial distances of fasteners to fast_cg
    F_xi = get_F_x(F_x)  # force per fastener
    F_zi = get_F_z(F_z)  # force per fastener
    for i in range(A_i.__len__()):
        r_i.append(get_r_i(x_i[i], z_i[i]))  # determine radial distances
    for i in range(A_i.__len__()):
        F_M_yi = get_F_M_y(M_y, A_i[i], r_i[i], A_i, r_i)  # moment per fastener
        loads.append([F_xi, F_zi, F_M_yi])
        # The three functions give two forces and a moment per fastener
    configs_loads.append(loads)
    loads = []

