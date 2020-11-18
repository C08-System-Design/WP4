import math
#this file will calculate the fasterner pattern
#hole locations
z_i = [0.03, -0.03]     #count from largest positive hole
x_i = [0.08]    #count positive from side

#base plate geometry
w = 0.1         #width of base plate
length = 0.5    #length of base plate
t2 = 0.01   #thickness of base plate

#margin to edge
top = w-z_i[0]
side = length/2 -x_i[0]
print top,side
col = len(x_i)  #column each side
row = len(z_i)  #holes per column
n = col * row   #hole each side

#material property
TYS = 276000000  #Tensile Yield Stress
ratio = 0.55
SYS = ratio * TYS   #Shear Yield Stress

#margins
SF = 2  #safety factor
SC = 3  #stress concentration
Pi = math.pi
F = 2600
V = F
#rivet snap failure
V_each = V / (n * 2)
V_each_eff = V_each * SC * SF
D_1 = 2*math.sqrt(V_each_eff/Pi/SYS)
print D_1

#shear out failure
tau_top = V_each_eff / 2 / top / t2
tau_side = V_each_eff / 2 / side / t2
if tau_top <= SYS and tau_side <= SYS:
    print "shear out ok"
else:
    print "shear out failure"

#compressive
D_2 = V_each_eff/ t2 / TYS
print D_2