plate_width = float(1) #fake value
plate_length = 0.3  #fake value
h = 0.0848
t_1 = 0.02         #fake value
t_1_margin = 0.5    #fake value
c_to_c = [2,3]         #centre to centre to hole diameter ratio
c_to_e = 1.5        #centre to edge to hole diameter ratio
n = 4               #fake value total number of holes always even number
n_each = int(n/2)     #number of holes each side
UL = 0.5*plate_length-(1+t_1_margin)*t_1-0.5*h
configs = []

for rows in range(1,4):
    for cols in range(1,4):
        for c2c in c_to_c:
            Z_ratio = (rows-1) * c2c + 2 * c_to_e
            X_ratio = c_to_e+(cols-1)*c2c+0.5
            D_z = plate_width/Z_ratio
            D_x = UL/X_ratio
            D = min(D_z, D_x)

            z_i = [-0.5 * plate_width + c_to_e * D_z]
            for i in range(1, rows):
                z_i.append(z_i[i - 1] + c2c * D_z)
            z_i_per = [i / plate_width for i in z_i]
            z_i = [round(i, 2) for i in z_i]

            x_j = [UL-c_to_e*D_x+0.5*h+t_1*(1+t_1_margin)]
            for j in range(1, cols):
                x_j.append(x_j[j - 1] - c2c * D_x)
            x_j_per = [j / (0.5*plate_length) for j in x_j]
            x_j = [round(i,2) for i in x_j]
            for k in range(0, cols):
                x_j.append(-x_j[cols - k-1])
            coor = []
            for z_coor in z_i:
                for x_coor in x_j:
                    coor.append([z_coor,x_coor])
            print(cols,"cols", rows,"rows")
            print ("c2c is",c2c)
            print ("coor list (z,x)", coor)
            print()




            #print z_i
            #print x_j
