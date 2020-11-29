from D406 import *
from math import sqrt


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

# Override
t_2 = []
for i in range(18):
    t_2.append(0.005)
# print(sigma_br(P_i, D, t_2)[17], "MPa")

# t_2 = []
# for t in range(18):
#     t_2.append((t+1)/1000)
# c = 0
# for i in sigma_br(P_i, D, t_2):
#     c += 1
#     if i >= (mat.get("sigma_ult")):
