import itertools
from mesh import *

opt = []
c = 0
# f = open()
for mesh in gen_meshes(D, D_mult, sizes):
    try:
        print("LEN:", len(mesh))
        for r in range(len(mesh) + 1):
            if r > 16:
                break
            else:
                combs_object = itertools.combinations(mesh, r)
                combs_lst = list(combs_object)
                c += 1
                print(c)
    except TypeError:
        None
