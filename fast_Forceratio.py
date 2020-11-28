def forceratio(E_a,E_b):
    
    #input = youngs mod of material for attach syst, youngs mod of fastener mat
    
    ''' Force ratio '''
    import numpy as np

    #Variables for Compliance of attachment mechanism

    D_fo = #outer diam of fast
    D_fi = #outer diam of fast
    t_2 = #thickness of back-plate


    '''Calc of attachment compliance'''
    da = 4*t_2 / (E_a*np.pi*(D_fo**2 - D_fi**2))




    #Variables for Compliance of fastener 

    d = D_fi #diameter of head/nut
    A_sha = np.pi * (d/2)**2 #cross-sect area of shank 
    L_sha = #length of shank 
    A_nom = np.pi * (D_fo /2)**2 #nominal cross-sect area of head/nut
    A_3 = A_sha #area for engaged shank


    '''Calc of fastener compliance'''

    L_hsub = 0.5*d
    L_engsub = 0.4*d
    L_nsub = 0.4*d

    db = 1/E_b * (L_hsub/A_nom + L_engsub/A_3 + L_sha/A_sha) + L_nsub/(E_b * A_nom)
    
    #Force ratio

    phi = da / (da+db)

return(phi)


