"""
pick a coordinate system (cs)
    my guess is that in the centre of the xz plane is best
    and symmetric over both the x axis and z axis
import coordinates x_i , z_i of fasteners
select a fastener diameter (are all the same?)
get area
get x_cg , z_cg
"""
from pattern import configs, D
# configs is a list with lists (configurations) containing two lists (x_i, z_i)
# D is diameter of fasteners, all fasteners have the same diameter


def get_A_f(D):  # area of a fastener
    A = D**2/4
    return A


def get_x_cg(A, x):  # A and x are lists
    if sum(A) == 0:
        x_cg = 0  # accounts for the case when x is 0
    else:
        x_cg = sum(A)*sum(x)/sum(A)
    return x_cg


def get_z_cg(A, z):  # A and z are lists
    if sum(A) == 0:
        z_cg = 0  # accounts for the case when z is 0
    else:
        z_cg = sum(A)*sum(z)/sum(A)
    return z_cg


cgs_x = []
cgs_z = []
for config in configs:
    x_i = config[0]
    z_i = config[1]
    D_i = [D]  # are all the same?
    A_i = []
    for i in D_i:
        A_i.append(get_A_f(i))

    cgs_x.append(round(get_x_cg(A_i, x_i), 3))
    cgs_z.append(round(get_z_cg(A_i, z_i), 3))
    # important to maintain order! A_i correspond to x_i and z_i
    # if we select different fasteners, does area scale with mass appropriately
print(cgs_x)
print(cgs_z)
