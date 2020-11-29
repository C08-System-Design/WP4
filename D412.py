from D406 import *
from D410 import phi_b, phi_w
from D411 import *
from math import sqrt
from sympy import *

# calculating the resulting force due to thermal and mechanical loading
# Currently done for A8090_T8151
# It is assumed that the in plane mechanical forces act in the same direction
# as the thermal stresses so that it gives a conservative answer.


def res_load(Fm, Ft):  # resulting load
    F = Fm + Ft
    return F


Fs = []
for i in range(18):
    Fs.append(res_load(loads_mag[i], max(abs(minTLs[i]), maxTLs[i])))


# gives the highest combined loading magnitude for each configuration
# this is then taken to 407 again
