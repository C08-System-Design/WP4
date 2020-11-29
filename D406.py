from D403 import *  # retrieve loads
from D404 import configs, D
from math import sqrt, pi
# import from D405 not necessary as we know the CG did not change


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

loads_mag = []  # magnitude of vector sum of mechanical loads of every config
temp = 0
for i in configs_loads:
    loads_mag.append(sqrt(i[0][0]**2+i[0][1]**2))
    # considering only F_x and F_y since the moment is irrelevant

