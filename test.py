D = []  # list of diameters over which we shall iterate
D_min = 1e-2  # [m]
D_max = 2e-2  # [m]
dD = 1e-3  # step in D
while D_min <= D_max:
    D.append(D_min)
    D_min += dD

print(D)
