from mat import pi
from push_check.py import max_Fyi
from     import Nf #imported from other code

def get_sigma (Fy, A_zx):
    sigma_xz = Fy / A_zx  # normal stress due to Fyi
    return sigma_xz

def get_tau (Fy, A_y):
    tau_y = Fy / A_y  # shear force that counters normal stress (due to Fyi)
    return tau_y

Fy = max_Fyi #use maximum loaded fastener


#values need to be put in still
D_fo =
D_fi =
t2 =      #thickness from spacecraft wall
t3 =      #thickness from lug wall
sigma_yield =     #depends on material type
tau_yield =       #depends on material type

A_zx = 1/4 * pi *(D_fo**2 - D_fi**2) #area normal stress works on
A_y2 = pi * D_fi * t2 #area shear stress works on with thickness t2
A_y3 =  pi * D_fi * t2 #area shear stress works on with thickness t3 (shear stress is calculated for both plates on their own)


sigma_xz = get_sigma(Fy, A_zx) #calc norm stress
tau_y_2 = get_tau(Fy, A_y2)    #calc shear stress for back plate
tau_y_3 = get_tau(Fy, A_y3)    #calc shear stress for lug plate

#check if shear stresses are too high
if tau_y_2 > tau_yield:
    print("the shear stress is too high for thickness 2")
    print(tau_y_2 + " vs " + tau_yield)
if tau_y_3 > tau_yield:
    print("the shear stress is too high for thickness 3")
    print(tau_y_3 + " vs " + tau_yield)





