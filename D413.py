"""
This is the ultimate file. The file that runs iterations on every possible
combination of the lug design. It considers:
o lug dimensions,
o back-up wall bearing checks,
o back-up wall bearing checks including thermal loads
o back-up wall pull-through checks,
o vehicle wall bearing checks including thermal loads (this is zero difference)
o vehicle wall pull-through checks.  RIGHT?
"""

from mat import *
from D412 import *
from D414 import mat

s = 0  # a variable to track scores
D = []
t = []
w = []
MS_obl = []
MS_bend = []
for mat in mats:
    D.append(getlugdimensions(mat.get("sigma_y"), mat.get("sigma_ult"))[0])
    t.append(getlugdimensions(mat.get("sigma_y"), mat.get("sigma_ult"))[1])
    w.append(getlugdimensions(mat.get("sigma_y"), mat.get("sigma_ult"))[2])
    MS_obl.append(getlugdimensions(mat.get("sigma_y"), mat.get("sigma_ult"))[3])
    MS_bend.append(getlugdimensions(mat.get("sigma_y"), mat.get("sigma_ult"))[4])


# thickness is iterated until the code gives reasonable
print("--------------------------------------------")
print("Rerunning D407 for the new loading from D412")
print("--------------------------------------------")

D = []
for config in configs:
    D.append(config[2])  # 18 different diameters for 18 fastener patterns

t_2 = []
for t in range(18):
    t_2.append((t+1)/10000)

c = 0
for i in sigma_br(Fs, D, t_2):
    c += 1
    if i >= (mat.get("sigma_ult")):
        None
        # print("Error in D407: In-plane loads are too high, increase thickness "
        #       "or reduce loading for config", c)
    print(round(i, 3), "MPa is the in-plane stress experienced in config", c)
    MS = mat.get("sigma_ult")/i-1
    print("MS is", MS)

print("-----------------")
print("CALCULATED DIMENSIONS")
print("-----------------")

cn = 3  # number of the configuration selected
t_1 = t_1  # defined earlier
t_2 = t2  # defined earlier
t_3 = t3  # defined earlier, edit both in D409
D_1 = getlugdimensions(mat.get("sigma_y"), mat.get("sigma_ult"))[0]
D_2 = configs[cn-1][2]
w_1 = getlugdimensions(mat.get("sigma_y"), mat.get("sigma_ult"))[2]
w_2 = w_1
l = 0.03  # [m]
l_1 = l
l_2 = plate_length
h = h  # defined previously
print(round(t_1, 5), "lug thickness in m")
print(round(t_2, 5), "backplate thickness in m")
print(round(t_3, 5), "wall thickness in m")
print(round(D_1, 5), "lug hole diameter in m")
print(round(D_2, 5), "fastener hole diameter in m")
print(round(w_1, 5), "lug width in m")
print(round(w_2, 5), "backplate width in m")
print(round(l_1, 5), "lug length in m")
print(round(l_2, 5), "backplate length in m")
print(round(h, 5), "spacing between the two lugs in m")
print(configs[cn-1][3][0]*configs[cn-1][3][1]*2, "is the number of fasteners")
print(configs[cn-1][3][0], "is the number of rows of fasteners")
print(configs[cn-1][3][1]*2, "is the number of columns of fasteners")
print(configs[cn-1][3][2], "is the c2c parameter")
print(configs[cn-1][0], "are the x_i coordinates of fasteners")
print(configs[cn-1][1], "are the z_i coordinates of fasteners")

"""
Margins of safety
"""
