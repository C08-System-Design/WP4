A7705_T6 = \
    {"rho": 2.81,  # Density in kg/m^3
     "E": 71.7,  # Young's modulus in GPa
     "sigma_ult": 510,  # Ultimate tensile strength in MPa
     "sigma_y": 430,  # Yield strength in MPa
     }

A6061_T6 = \
    {"rho": 2.7,  # Density in kg/m^3
     "E": 69,  # Young's modulus in GPa
     "sigma_ult": 310,  # Ultimate tensile strength in MPa
     "sigma_y": 270,  # Yield strength in MPa
     }

Ti_6Al_4V = \
    {"rho": 4.5,  # Density in kg/m^3
     "E": 104,  # Young's modulus in GPa
     "sigma_ult": 900,  # Ultimate tensile strength in MPa
     "sigma_y": 880,  # Yield strength in MPa
     }

mats = [A7705_T6, A6061_T6, Ti_6Al_4V]

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
