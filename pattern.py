plate_width = float(0.1) #fake value
plate_length = 0.2  #fake value
h = 0.0848
t_1 = 0.02          #fake value
t_1_margin = 0.5    #fake value
c_to_c = 2         #centre to centre to hole diameter ratio
c_to_e = 1.5        #centre to edge to hole diameter ratio
n = 4               #fake value total number of holes always even number
n_each = int(n/2)     #number of holes each side
UL = 0.5*plate_length-(1+t_1_margin)*t_1-0.5*h

#first configuration, holes align one column in x axis n*1
D_2 = plate_width/(((n_each-1) * c_to_c)+3)
x_i = [-0.5*plate_width+1.5*D_2]
print D_2
for i in range(1, n_each):
    x_i.append(x_i[i-1]+c_to_c*D_2)

x_i_per = [i/plate_width for i in x_i]
print "location percentage of the holes and width direction"
print x_i_per

if 3*D_2 >= UL:
    D_2 = UL/3
    print "buzzzz"      #UL constrain

print D_2

#second configuration, holes align two column in x axis n*2


