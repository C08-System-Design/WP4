w = 0.05
D = 0.02
t_1 = 0.005

a_1 = (w-D/(2**0.5))/2
a_2 = (w-D)/2

A_av = 6/((3/a_1)+(1/a_1)+(2/a_2))*t_1
A_br = D*t_1

A_ratio = A_av/A_br
print A_ratio
K_ty = 0.546875 * A_ratio**4 - 1.55308 * A_ratio**3 + 1.03647 * A_ratio**2 + 1.00695 * A_ratio - 0.000214487
print K_ty
from mat import A7075_T6 as mat
print A7075_T6.get("rho")