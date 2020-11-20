from fast_loads import A_i, x_i, z_i, r_i
from  import Mz, Nf, Fy

def get_Fpi(Fy, Nf): #eq 4.6
    Fpi = Fy / Nf
    return Fpi

def get_sumAr2(Ai, ri, Nf): #parameter needed in eq 4.7
    sumAr2 = sum(Ai[i]*ri[i]*ri[i] for i in range(Nf))
    return sumAr2

def get_FpMz(Mz, A, x, r): #4.7
    sign = abs(x) / x #positive is tension, negative is compression
    FpMz = sign * Mz * A * r / sumAR2
    return FpMz


sumAR2 = get_sumAr2(Ai, ri, Nf)

Fyi = []
for i in range(Nf): #calc for each hole
    Fpi = get_Fpi(Fy, Nf)
    FpMz = get_FpMz(Mz, Ai[i], xi[i], ri[i])
    Fyi.append(Fpi + Fmpz)

max_Fyi = max(Fyi)
max_Fyi_index = Fyi.index(max_value)

print(Fyi)

print("the fastener with the highest load is on coordinates (x,z):" + xi[max_Fyi_index] + " , " + zi[max_Fyi_index])