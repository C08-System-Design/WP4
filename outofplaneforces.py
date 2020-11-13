from    import Ai, xi, zi, ri, Mz, Nf, Fy

def get_Fpi(Fy, Nf):
    Fp = Fy / Nf
    Fpi = []
    for i in range(Nf):
        Fpi.append(Fp)
    return Fpi

def get_sumAr2(Ai, ri, Nf):
    sumAr2 = sum(Ai[i]*ri[i]*ri[i] for i in range(Nf))
    return sumAr2

def get_FpMz(Mz, A, x, r):
    sign = abs(x) / x
    FpMz = sign * Mz * A * r / sumAR2
    return FpMz


sumAR2 = get_sumAr2(Ai, ri, Nf)

for i in range(Nf):
    Fpi = get_Fpi(Fy, Nf)
    FpMz = get_FpMz(Mz, Ai[i], xi[i], ri[i])
    Fyi = []
    Fyi.append(Fpi + FpMz)

max_value = max(Fyi)
max_index = Fyi.index(max_value)

print(Fyi)

print("the fastener with the highest load is on coordinates (x,z):" + xi[max_index] + " , " + zi[max_index])