from fast_stress import *


def get_Fpi(Fy, Nf): #eq 4.6 in reader
    Fpi = Fy / Nf
    return Fpi


def get_sumAr2(Ai, ri, Nf):  #parameter needed in eq 4.7
    sumAr2 = sum(Ai[i]*ri[i]*ri[i] for i in range(Nf))
    return sumAr2


def get_FpMz(Mz, A, x, r, sumAR2): # equation 4.7
    sign = abs(x) / x  #positive is tension, negative is compression
    FpMz = sign * Mz * A * r / sumAR2
    return FpMz


max_Fyi = []
for config in configs:
    Nf = len(config[0])
    sumAr2 = get_sumAr2(A_i, r_i, Nf)  #calculate parameter beforehand

    Fyi = []
    for i in range(Nf):  #calc for each hole
        Fpi = get_Fpi(F_y, Nf)
        FpMz = get_FpMz(M_z, A_i[i], x_i[i], r_i[i], sumAr2)
        Fyi.append(Fpi + FpMz)  #add sum of both forces to final result list

    #calculate fastener hole with the maximum load
    max_Fyi.append(max(Fyi))
    # max_Fyi_index = Fyi.index(max_Fyi)

# print(max_Fyi)

# print("the fastener with the highest load is on coordinates (x,z):"
#       + xi[max_Fyi_index] + " , " + zi[max_Fyi_index])