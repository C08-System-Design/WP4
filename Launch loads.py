'Determination of the launch loads'
def orbitloads():
    import numpy as np
    'Set uo the given data'

    omega = 1 #deg/s
    CMG_torque = 45 #Nm
    Spacecraft_radius = 1.19#m
    SA_mass = 22.34 #kg
    SA_length = 2.3255 #m
    I_spacecraft = 1050.101 #kgm^2


    'Calculations'
    #get right units
    
    omega_rad = omega / (360/(2*np.pi))
    

    #EOM to get max accelaration
    alpha_max = CMG_torque / I_spacecraft

    #from given --> max rotational speed should be 1 deg/s

    'Max load in normal direction'
    F_norm = (((omega_rad * (Spacecraft_radius + SA_length/2))**2) / (Spacecraft_radius + SA_length/2)) * SA_mass

    'Max load in tangent direction'
    F_tan = alpha_max*(Spacecraft_radius + SA_length/2)*SA_mass

    print(F_tan, F_norm,)

    return

orbitloads()
    
