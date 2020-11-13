"""
pick a coordinate system (cs)
    my guess is that in the centre of the xz plane is best
import coordinates x_i , z_i of fasteners
select a fastener diameter (are all the same?)
get area
get x_cg , z_cg
"""


def get_Af(D):  # area of a fastener
    A = D**2/4
    return A


def get_x_cg(A, x):  # A and x are lists
    x_cg = sum(A)*sum(x)/sum(A)
    return x_cg


def get_z_cg(A, z):  # A and z are lists
    z_cg = sum(A)*sum(z)/sum(A)
    return z_cg


x_i = []
z_i = []
D_i = []  # are all the same?
A_i = []
for i in D_i:
    A_i.append(get_Af(i))

get_x_cg(A_i, x_i)
get_z_cg(A_i, z_i)
# important to maintain order! A_i correspond to x_i and z_i
