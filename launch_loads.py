#############################################################################################################################################
# All values ar retrieved from launch data parameterically so no changes have to be made in this file if a parameter in launch load changes #
#############################################################################################################################################

import math
from launch_data import *

m = 0.5 * m

def load(m, g, Load, FLL):
    force = m * g * Load * FLL
    return force

long_force = load(m, g, long_load, FLL)     # Longitudinal Force
lat_force = load(m, g, lat_load, FLL)       # Lateral Force

print(long_force)
# print(lat_force)