from fast_loads import A_i, x_i, z_i, r_i
from  import Mz, Nf, Fy  #import from other codes? should have been calculated already

def get_Fpi(Fy, Nf): #eq 4.6 in reader
    Fpi = Fy / Nf
    return Fpi

def get_sumAr2(Ai, ri, Nf): #parameter needed in eq 4.7
    sumAr2 = sum(Ai[i]*ri[i]*ri[i] for i in range(Nf))
    return sumAr2

def get_FpMz(Mz, A, x, r, sumAR2): # equation 4.7
    sign = abs(x) / x #positive is tension, negative is compression
    FpMz = sign * Mz * A * r / sumAR2
    return FpMz


sumAR2 = get_sumAr2(Ai, ri, Nf) #calculate parameter beforehand. since it is same for every fastener

Fyi = []
for i in range(Nf): #calc for each hole
    Fpi = get_Fpi(Fy, Nf)
    FpMz = get_FpMz(Mz, Ai[i], xi[i], ri[i], sumAR2)
    Fyi.append(Fpi + Fmpz) #add sum of both forces to final result list

#calculate fastener hole with the maximum load
max_Fyi = max(Fyi)
max_Fyi_index = Fyi.index(max_value)

print(Fyi)

print("the fastener with the highest load is on coordinates (x,z):" + xi[max_Fyi_index] + " , " + zi[max_Fyi_index])