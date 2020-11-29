"""All values ar retrieved from launch data parametrically so no changes have
to be made in this file if a parameter in launch load changes"""


m = 22.3449         # mass of satellite
g = 9.81            # gravitational acceleration
long_load = 7.5     # experienced amount of G's in longitudinal direction
lat_load = 1.5      # experienced amount of G's in lateral direction
FLL = 3.2175        # the safety factor (this is the highest factor -->
# --> ultimate Load - but can be changed to Yield Load 2.68125)

m = 0.5*m
d_z = 0.6  # estimated from CATIA, dist from CG to lug in z axis


def load(m, g, Load, FLL):
    force = m * g * Load * FLL
    return force


F_x = load(m, g, lat_load, FLL)  # Lateral Force
F_y = F_x  # equal lateral loading
F_z = load(m, g, long_load, FLL)  # Longitudinal Force
M_x = 0  # the solar array is free to rotate around this axis, but held in
# place by a reactionary moment of the solar array drive mechanism
M_y = 0  # the mass is equally distributed, so the moments should cancel
M_z = F_x*d_z
