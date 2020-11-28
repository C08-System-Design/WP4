from mat import *
from push_check import max_Fyi
from push_check import *


def get_sigma(Fy, A_zx):
    sigma_xz = Fy / A_zx  # normal stress due to Fyi
    return sigma_xz


def get_tau(Fy, A_y):
    tau_y = Fy / A_y  # shear force that counters normal stress (due to Fyi)
    return tau_y


# values need to be put in still
c = 0
for config in configs:
    F_y = max_Fyi[c]  # use maximum loaded fastener
    c += 1
    D_fo = config[2]+config[2]*0.4
    D_fi = config[2]
    t2 = 0.001  # thickness from spacecraft wall
    t3 = 0.001  # thickness from lug wall
    sigma_yield = A7075_T6.get("sigma_y")  # depends on material type
    tau_yield = A7075_T6.get("ratio")*A7075_T6.get("sigma_y")

    A_zx = 1/4 * pi * (D_fo**2 - D_fi**2)  # area normal stress works on
    A_y2 = pi * D_fi * t2  # area shear stress works on with thickness t2
    A_y3 = pi * D_fi * t2  # area shear stress works on with thickness t3
    # (shear stress is calculated for both plates on their own)

    sigma_xz = get_sigma(F_y, A_zx)  # calc norm stress
    tau_y_2 = get_tau(F_y, A_y2)    # calc shear stress for back plate
    tau_y_3 = get_tau(F_y, A_y3)    # calc shear stress for lug plate

    # check if shear stresses are too high
    if tau_y_2 > tau_yield:
        print("the shear stress is too high for thickness 2")
        print(tau_y_2 + " vs " + tau_yield)
    if tau_y_3 > tau_yield:
        print("the shear stress is too high for thickness 3")
        print(tau_y_3 + " vs " + tau_yield)





