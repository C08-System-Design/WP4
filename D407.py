from D406 import *
from mat import *
from math import sqrt

# sigma_br = P_i/D_2/t_2  # in-plane force / fast dia / backplate thickness
# get bearing allowable - different for every material
# verify D_2 and t_2, can be reduced to optimize mass
# do it for both the backup wall and spacecraft wall
# verify that not more fasteners are needed
# higher thickness can be only at a section of the wall

# --- Import --- #
# import lug geometry and fast dia
# setup wall geometry
t_wall = 0.01  # [m]


def get_P_i(load):
    Pi = sqrt(load[0]**2+load[1]**2)
    return Pi


def sigma_br(P, Dia, thickness):
    sigma = []
    for i in range(18):
        sigma.append(P[i]/Dia[i]/thickness[i]/1e6)  # MPa conversion
    return sigma


P_i = []
for config in configs_loads:
    P_i.append(get_P_i(config[0]))  # vector sum of in plane loads per fastener
    # in each configuration (fastener pattern)

D = []
for config in configs:
    D.append(config[2])  # 18 different diameters for 18 fastener patterns

t_2 = []
for t in range(18):
    t_2.append((t+1)/1000)
# print(sigma_br(P_i, D, t_2), "MPa")
