import pandas as pd
from math import pi
from math import exp
import matplotlib.pyplot as plt


def get_rho(z):
    dens = exp(A*z**4+B*z**3+C*z**2+D*z+E)
    return dens


def get_drag(z, dens):
    vel = (mu/(R_E+z))**(1/2)
    drag = 1/2*C_D*A_D*dens*vel**2
    return drag


def get_g(z):
    g = g_0*(R_E/(R_E+z))**2
    return g


def get_E(z):
    energy = 1/2*m*mu/(R_E+z*1000)+m*g_0*(R_E/(R_E+z*1000))**2*z*1000
    return energy


# ----- Initial values ----- #
f = pd.read_csv("exosphere_dat.csv", sep=";")
mu = 3.986e14
m = 987
h = 4.5e5
R_E = 6.378e6
g_0 = 9.80665
C_D = 2.2  # coefficient of drag, taken from books
A_D = 6.8  # 10.8 is solar array, 2.8 + 2*2 is the S/C
stp = [86, 91, 100, 110, 120, 150, 200, 300, 500, 750, 1000]

# ----- Initial Parameters ----- #
R_0 = h + R_E
V_0 = (mu/R_0)**(1/2)
T_0 = 2*pi*R_0/V_0

# ----- Atmospheric Descent ----- #
# --- Density Model --- #
#  for density, source http://www.braeunig.us/space/atmmodel.htm#modeling

i = 0
rho_lst = []
alt_lst = []
for x in stp:
    A = f.A[i]
    B = f.B[i]
    C = f.C[i]
    D = f.D[i]
    E = f.E[i]
    step = 0
    while stp[i]+step <= stp[i+1]:
        rho = get_rho(x+step)
        rho_lst.append(rho)
        alt_lst.append(stp[i]+step)
        step += 1
        if stp[i]+step > h/1000:
            break
    if stp[i]+step > h/1000:
        break
    i += 1

plt.plot(alt_lst, rho_lst)
plt.xlabel("Altitude [km]")
plt.ylabel("Density [kg/m3]")
plt.savefig("rho_vs_alt")
plt.clf()

# some inaccuracy on the 100-110 km range, but fine
# --- Drag Model --- #
t_0 = 0  # [s]
drag_lst = []
i = 0
for x in alt_lst:
    rho = rho_lst[i]
    drag_lst.append(get_drag(x * 1000, rho))
    i += 1

plt.plot(alt_lst, drag_lst, "r")
plt.xlabel("Altitude [km]")
plt.ylabel("Drag [N]")
plt.savefig("drag_vs_alt")
plt.clf()

# --- Deorbit Time --- #
E = 1/2*m*V_0**2 + m*get_g(h)*h
c = rho_lst.__len__()
t_lst = []
for i in alt_lst[::-1]:
    dE = abs(get_E(i) - get_E(i+1))
    dt = dE/(get_drag(i, rho_lst[c-1])*(mu/(R_E+i))**(1/2))
    c -= 1
    t_lst.append(dt)
    if i < 100:
        break

# ----- Results ----- #
print("It will take roughly", round(sum(t_lst)/3600/24/365, 2),
      "years for the ESO to deorbit.")
w = open("exosphere_dat.txt", "w")
for i in range(alt_lst.__len__()):
    w.write(str(alt_lst[i]))
    w.write("\n")
w.write("-----DENSITY-----"+"\n")
for i in range(rho_lst.__len__()):
    w.write(str(rho_lst[i]))
    w.write("\n")

print(alt_lst[622])
print(rho_lst[622])
