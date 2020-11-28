from fast_loads import *
from mat import *

# sigma_br = P_i/D_2/t_2  # in-plane force / fast dia / lug_thickness
# get bearing allowable - different for every material
# verify D_2 and t_2, can be reduced to optimize mass
# do it for both the backup wall and spacecraft wall
# verify that not more fasteners are needed
# higher thickness can be only at a section of the wall

# --- Import --- #
# import lug geometry and fast dia
# setup wall geometry
t_wall = 0.01  # [m]
