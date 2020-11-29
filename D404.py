from D403 import *
from D414 import mat

w = getlugdimensions(mat.get("sigma_y"), mat.get("sigma_ult"))[2]
plate_width = w
plate_length = 0.1  # arbitrary
h = 0.02
t_1 = getlugdimensions(mat.get("sigma_y"), mat.get("sigma_ult"))[1]
t_1_margin = 0
c_to_c = [2, 3]  # centre to centre to hole diameter ratio
c_to_e = 1.5  # centre to edge to hole diameter ratio
n = 4  # fake value total number of holes always even number
n_each = int(n/2)  # number of holes each side
UL = 0.5*plate_length-(1+t_1_margin)*t_1-0.5*h
# useable length each side, half length minus half h and t, and also t margin
configs = []

for rows in range(1,4):
    for cols in range(1,4):
        for c2c in c_to_c:
            config = []
            Z_ratio = (rows-1) * c2c + 2 * c_to_e
            # c2e D + c2c*D for each c2c + c2e D
            X_ratio = c_to_e+(cols-1)*c2c+0.5
            # 0.5 D+ c2c*D for each c2c + c2e D
            D_z = plate_width/Z_ratio
            D_x = UL/X_ratio
            D = min(D_z, D_x)

            z_i = [-0.5 * plate_width + c_to_e * D_z]
            for i in range(1, rows):
                z_i.append(z_i[i - 1] + c2c * D_z)
            z_i_per = [i / plate_width for i in z_i]
            # percentage location of the holes and z not using now
            z_i = [round(i, 4) for i in z_i]

            x_j = [UL-c_to_e*D_x+0.5*h+t_1*(1+t_1_margin)]
            for j in range(1, cols):
                x_j.append(x_j[j - 1] - c2c * D_x)
            x_j_per = [j / (0.5*plate_length) for j in x_j]
            # percentage location of the holes and x not using now
            x_j = [round(i,4) for i in x_j]

            for k in range(0, cols):  # mirror column to other side
                x_j.append(-x_j[cols - k-1])
            coor = []
            for z_coor in z_i:  # create coor list from column and row location
                for x_coor in x_j:
                    coor.append([z_coor,x_coor])

            x_a = [i[1] for i in coor]  # x only list
            z_a = [i[0] for i in coor]  # z only list
            k_a = [cols,rows,c2c]
            config = [x_a,z_a,D,k_a]