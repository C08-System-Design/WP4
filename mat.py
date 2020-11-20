A7705_T6 = \
    {"rho": 2810,  # Density in kg/m^3
     "E": 71.7,  # Young's modulus in GPa
     "sigma_ult": 510,  # Ultimate tensile strength in MPa
     "sigma_y": 430,  # Yield strength in MPa
     "alpha": ,   #thermal exp coef in 1/K
     }

A6061_T6 = \
    {"rho": 2700,  # Density in kg/m^3
     "E": 69,  # Young's modulus in GPa
     "sigma_ult": 310,  # Ultimate tensile strength in MPa
     "sigma_y": 270,  # Yield strength in MPa
     "alpha":   ,   #thermal exp coef in 1/K
     }

Ti_6Al_4V = \
    {"rho": 4500,  # Density in kg/m^3
     "E": 104,  # Young's modulus in GPa
     "sigma_ult": 900,  # Ultimate tensile strength in MPa
     "sigma_y": 880,  # Yield strength in MPa
     "alpha":   ,   #thermal exp coef in 1/K
     }
A2195_T84 = \
    {"rho": 2700,  # Density in kg/m^3
     "E": 78,  # Young's modulus in GPa
     "sigma_ult": 525,  # Ultimate tensile strength in MPa
     "sigma_y": 490,  # Yield strength in MPa
     "alpha": ,   #thermal exp coef in 1/K
     }

Steel = \
    {"rho": 7800,  # Density in kg/m^3
     "E": 207,  # Young's modulus in GPa
     "sigma_ult": ,  # Ultimate tensile strength in MPa
     "sigma_y": ,  # Yield strength in MPa
     "alpha": 13.3*10^(-6),   #thermal exp coef in 1/K
     }

mats = [A7705_T6, A6061_T6, Ti_6Al_4V, A2195-T84,Steel]

"""
This code stores all defined materials (mats) in a list called mats.
Items in this list are dictionaries containing properties of a single material.
To get these properties, use the .get method with argument being your property.
For example:
"""
A7705_T6.get("rho")
"""
To iterate over the list of all materials, you do the following:
"""
for mat in mats:
    mat.get("rho")
"""
For now, my suggestion would be to import a single material into your code using
    from mat import Al6061_T6 as mat
and use mat.get("yourwantedproperty")
"""
