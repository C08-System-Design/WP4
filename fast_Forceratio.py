def forceratio(E_a,E_b):
    
    #input = youngs mod of material for attach, youngs mod of mat for fast
    
    ''' Force ratio '''
    import numpy as np

    #Variables for Compliance of attachment mechanism

    D_fo = #outer diam of fast
    D_fi = #outer diam of fast
    t = #thickness of ...
    E_a = #young's mod of attachment mechanism


    '''Calc of attachment compliance'''
    da = 4*t / (E_a*np.pi*(D_fo**2 - D_fi**2))




    #Variables for Compliance of fastener 

    E_b = #youngs mod of fast mat
    d = #diameter of head/nut
    A_sha1 = #cross-sect area of shank 1
    A_sha2 = 0 #cross-sect area of shank 2
    L_sha1 = #length of shank 1
    L_sha2 = 0 #length of shank 2
    A_nom = #nominal cross-sect area
    A_3 = #area for engaged shank


    '''Calc of fastener compliance'''

    L_hsub = 0.5*d
    L_engsub = 0.4*d
    L_nsub = 0.4*d

    db = 1/E_b * (L_hsub/A_nom + L_engsub/A_3 + L_sha1/A_sha1 + L_sha2/A_sha2) + L_nsub/(E_b * A_nom)
    
    #Force ratio

    phi = da / (da+db)

return(phi)


