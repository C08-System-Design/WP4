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


def get_F_cg(Fx, Fz):
    F_cg = sqrt(Fx**2+Fz**2)
    return F_cg


def get_F_x(F):  # F = F_cgx 
    n = A_i.__len__()  # number of fasteners
    F_x = F/n
    return F_x


def get_F_z(F):  # F = F_cgz 
    n = A_i.__len__()  # number of fasteners
    F_z = F/n
    return F_z


def get_F_M_y(M, A, r, Ai, ri):  # M is moment, A is A_f, Ai and ri are lists
    # with all fasteners and r is fastener arm
    F_M_y = M*A*r/sum(Ai)/sum(ri)/sum(ri)
    return F_M_y


def get_r_i(x, z):
    r = sqrt(x**2+z**2)
    return r


# retrieve loads
F_x = 10
F_z = 0
M_y = 0  # TODO: M_y needs to be calculated

# retrieve fastener data
A_i = [2, 2, 2, 2]
x_i = [1, -1, -1, 1]
z_i = [1, 1, -1, -1]
r_i = []  # radial distances of fasteners to fast_cg

# calculate
get_F_x(F_x)  # force per fastener
get_F_z(F_z)  # force per fastener
for i in range(A_i.__len__()):
    r_i.append(get_r_i(x_i[i], z_i[i]))  # determine radial distances
for i in range(A_i.__len__()):
    get_F_M_y(M_y, A_i[i], r_i[i], A_i, r_i)  # determine moment per fastener
# The three functions give forces and moment per fastener
