# import w and h
# coordinate system has an origin in the centre of the lug
# x is positive to the left
# z is positive up
# I will generate a mesh for the ++ quadrant (top left)
# that quadrant will then copy all its fastener iterations symmetrically
# two constraints: distance from the edge is 1.5D
# horizontal (or vertical) distance is 2-3D between two fasteners


def gen_mesh(x, y, m, n):
    # x = diameter, y = diameter multiplier from 2 to 3, m = w, n = h
    xn = []
    zn = []
    wnew = m-1.5*x-y/2*x
    hnew = n-1.5*x-y/2*x
    nw = int(wnew/(2*x))  # number of points in width rounded down
    nh = int(wnew/(2*x))  # number of points in height rounded down
    if nw == 0 or nh == 0:
        return print("Your D is too small :O")
    xn_i = wnew/nw
    zn_i = hnew/nh
    stpx = xn_i
    stpz = zn_i
    while xn_i <= wnew:
        xn.append(round(xn_i, 2))
        xn_i += stpx
    while zn_i <= hnew:
        zn.append(round(zn_i, 2))
        zn_i += stpz
    return combine(xn, zn)
# this function works without arrays and cuts the edges automatically


def combine(x, y):  # x and y are lists, the function gives any combination
    comb = []
    for i in x:
        for j in y:
            comb.append([i, j])
    return comb


# we start at [0 ,0] = the origin
# after we are done with the mesh we cut off all the outer points
# because no fastener can be at the edge of the lug

D = []  # list of diameters over which we shall iterate
D_min = 0.01  # [m]
D_max = 0.02  # [m]
dD = 0.001  # step in D
while int(1000*D_min) <= int(1000*D_max):
    D.append(D_min)
    D_min = 1000*D_min
    D_min += 1000*dD
    D_min = D_min/1000

D_mult = []  # list with values between 2 and 3 (multipliers)
dD_mult = 0.1
D_mult_min = 2.0  # starter value for the multiplier
D_mult_max = 3.0  # end value for the multiplier
while D_mult_min <= D_mult_max:
    D_mult.append(D_mult_min)
    D_mult_min = 1000*D_mult_min
    D_mult_min += 1000*dD_mult
    D_mult_min = D_mult_min/1000

wrange = 1  # [m] is max width
hrange = 1  # [m] is max height
size_stp = 0.01  # [m] is the step in dimensioning
w_i = 0+size_stp  # can't start with a zero
h_i = 0+size_stp  # can't start with a zero
w = []
h = []
while w_i < wrange and h_i < hrange:
    w.append(w_i)
    h.append(h_i)
    w_i += size_stp
    h_i += size_stp
sizes = combine(w, h)
print(D)
print(D_mult)
for size in sizes:  # size[0] = w , size[1] = h
    for i in D:
        for j in D_mult:
            if 1.5*i+j*i <= size[0]/2:
                print(gen_mesh(i, j, size[0], size[1]))
            # else:
                # print("Your D is too big :O ")

# print(gen_mesh(0.1, 2, 0.6, 0.6)[0])
# print(gen_mesh(0.1, 2, 6, 4)[1])
