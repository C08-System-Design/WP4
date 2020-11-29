from D411 import *
from math import sqrt
from sympy import *


def res_load(Fm, Ft):  # resulting load
    F = Fm + Ft
    return F


Fs = []
for i in range(18):
    Fs.append(res_load(loads_mag[i], max(abs(minTLs[i]), maxTLs[i])))
