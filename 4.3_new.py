w = 0.05
D = 0.02
t_1 = 0.005
h = 0.0848
l = 0.1 #distance between centre of D to base plate

F_z = 2644.8
F_x = 529.0

a_1 = (w-D/(2**0.5))/2
print (a_1)
a_2 = (w-D)/2

A_av = 6/((3/a_1)+(1/a_1)+(2/a_2))*t_1
A_br = D*t_1

A_ratio = A_av/A_br
print (A_ratio)
K_ty = 0.546875 * A_ratio**4 - 1.55308 * A_ratio**3 + 1.03647 * A_ratio**2 + 1.00695 * A_ratio - 0.000214487
print (K_ty)
from mat import *
TYS = A7075_T6.get("sigma_y") * 10**6


F_ty = TYS

P_ty = K_ty * A_br * F_ty

print (P_ty)


I_zz = w * ((2*t_1+h)**3-(h)**3) / 12
I_xx = w**3 * t_1 /6

M_z = F_x * l
M_x = F_z * l

z = 0.5* w
x = 0.5*h + t_1

sigma_y = M_x * z /I_xx +M_z * x /I_zz
print(sigma_y/TYS)