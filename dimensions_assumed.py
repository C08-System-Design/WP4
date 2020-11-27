'''Dimension determination'''
import numpy as np

#Material properties
sigma_y = 510*10**6 #Mpa
sigma_ult = 590*10**6 #MPa
P_trans0 = 2644.8/2 #N, load per lug
P_axial0 = 529/2 #N, per lug

P_trans = P_trans0 *1.5
P_axial = P_axial0 *1.5
M_z = (1.05 + 0.03)* P_axial0

K_ty = 0.5 #from graph

'''Calculate A_br'''
A_br = P_trans / (sigma_y * K_ty)

#List for iteration over t/D ratio's
t_D = [0.4,0.3,0.2,0.15,0.12,0.1,0.08,0.06] #referred to as y
w_D = [2.5,2.75,3,3.25,3.5]
D = []
t = []
w = []
vol = []

#A_br = Dt = D*D*y
for y in t_D:
    D1 = np.sqrt(A_br/y)
    t1 = D1*y

    if t1>0.001:
        for x in w_D:
            w1 = D1*x

            if w1>0.01:

                A1 = 0.5*(w1-D1)*t1 + 0.5*D1*t1*(1-np.cos(np.pi/4))
                A2 = 0.5*(w1-D1)*t1

                A_av = 6 /((4/A1)+(2/A1))
                ratio = A_av/A_br

                if ratio > 0.4 or ratio == 0.4:
                    D.append(D1)
                    t.append(t1)
                    w.append(w1)
                    
                    v = (w1 * D1/2 - (( D1 / 2)**2 * np.pi)/2)*t1 + ((( w1 / 2)**2 * np.pi)/2 - (( D1 / 2)**2 * np.pi)/2)*t1
                    vol.append(v)


index_min = vol.index(min(vol))
D_opt = D[index_min]
t_opt = t[index_min]
w_opt = w[index_min]
print("Optimal D is:", D_opt, ",optimal t is:",t_opt, ",optimal w is:",w_opt)

t_D1 = t_opt/D_opt
w_D1 = w_opt/D_opt

print("t/D and w/D ratios are:", t_D1, w_D1)

#check bending moment
sigma_z = (M_z * t_opt / 2) / (1/12 * w_opt * t_opt**3)
w_new = w_opt
t_new = t_opt
while sigma_z > sigma_y:
    w_new = w_new + 0.0005
    t_new = t_new + 0.0001
    
    sigma_z = (M_z * t_new / 2) / (1/12 * w_new * t_new**3)
    
print('Haaaaaaaaalloooooo', sigma_z)

    
#newly found values
A_br = D_opt * t_new
D_new = w_new / w_D1

print("D is:", D_new, ",t is:",t_new, ",w is:",w_new)

#Check axial loads
#K values depend on t/D and w/D value --> choose correct one from graph
#Should be > 264.5 N each

P_tens = sigma_y * (w_new - D_new)*t_new * 0.94

P_br = sigma_ult * 1.1 * A_br

P_trans = A_br * sigma_y * K_ty

Axial = [P_tens,P_br]

#Margin of safety

MS = (1 /(((P_axial0/(min(Axial)))**1.6 + (P_trans0/P_trans)**1.6))**0.623) - 1

print(MS)







