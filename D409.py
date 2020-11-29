from D408 import *
from math import pi


def get_sigma(Fy, A_zx):
    sigma_xz = Fy / A_zx  # normal stress due to Fyi
    return sigma_xz


def get_tau(Fy, A_y):
    tau_y = Fy / A_y  # shear force that counters normal stress (due to Fyi)
    return tau_y


t2 = 0.0005  # thickness from spacecraft wall
t3 = 0.0005  # thickness from lug wall
c = 0
for config in configs:
    F_y = max_Fyi[c]  # use maximum loaded fastener
    c += 1
    D_fo = config[2]+config[2]*0.4
    D_fi = config[2]

    sigma_yield = mat.get("sigma_y")  # depends on material type
    tau_yield = mat.get("ratio")*mat.get("sigma_ult")

    A_zx = 1/4 * pi * (D_fo**2 - D_fi**2)  # area normal stress works on
    A_y2 = pi * D_fi * t2  # area shear stress works on with thickness t2
    A_y3 = pi * D_fi * t3  # area shear stress works on with thickness t3
    # (shear stress is calculated for both plates on their own)

    sigma_xz = get_sigma(F_y, A_zx)  # calc norm stress
    tau_y_2 = get_tau(F_y, A_y2)    # calc shear stress for back plate
    tau_y_3 = get_tau(F_y, A_y3)    # calc shear stress for lug plate

    print("Shear stress in the backplate:", tau_y_2/1e6, "MPa")
    print("Shear stress in the spacecraft wall:", tau_y_3/1e6, "MPa")
    print("Shear stress allowable:", tau_yield, "MPa")
    MS = tau_yield/(max(tau_y_2, tau_y_3)/1e6) - 1
    print("MS is", MS)
    print("-----------------------------")
