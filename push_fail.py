from mat import pi
from push_check.py import max_Fyi

def get_sigma (Fy, A_zx):
    sigma_xz = Fy / A_zx  # normal stress due to Fyi
    return sigma_xz

def get_tau (Fy, A_y):
    tau_y = Fy / A_y  # shear force that counters normal stress (due to Fyi)
    return tau_y

Fy = max_Fyi #use maximum loaded fastener
Nf =
D_fo =
D_fi =
t2 =   #thickness from spacecraft wall
t3 =   #thickness from lug wall

A_xz = 1/4 * pi *(D_fo**2 - D_fi**2) #area normal stress works on
A_y2 = pi * D_fi * t2 #area shear stress works on with thickness t4
A_y3 =  pi * D_fi * t2 #area shear stress works on with thickness t3

for i in range(Nf):
    sigma_xz = get_sigma(Fy, A_zx)
    tau_y_2 = get_tau(Fy, A_y2)
    tau_y_3 = get_tau(Fy, A_y3)
    sigma_yield =
    tau_yield =
    if tau_y_2 > tau_yield:
        print("for fastener " + i + " the shear stress is too high for thickness 2")
        print(tau_y_2 + " vs " + tau_yield)
    if tau_y_3 > tau_yield:
        print("for fastener " + i + " the shear stress is too high for thickness 3")
        print(tau_y_3 + " vs " + tau_yield)





