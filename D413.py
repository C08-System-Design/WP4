"""
This is the ultimate file. The file that runs iterations on every possible
combination of the lug design. It considers:
o lug dimensions,
o back-up wall bearing checks,
o back-up wall bearing checks including thermal loads
o back-up wall pull-through checks,
o vehicle wall bearing checks including thermal loads
o vehicle wall pull-through checks.  RIGHT?
"""

from mat import *
from D403 import *

s = 0  # a variable to track scores
D = []
t = []
w = []
MS_obl = []
MS_bend = []
for mat in mats:
    D.append(getlugdimensions(mat.get("sigma_y"), mat.get("sigma_ult"))[0])
    t.append(getlugdimensions(mat.get("sigma_y"), mat.get("sigma_ult"))[1])
    w.append(getlugdimensions(mat.get("sigma_y"), mat.get("sigma_ult"))[2])
    MS_obl.append(getlugdimensions(mat.get("sigma_y"), mat.get("sigma_ult"))[3])
    MS_bend.append(getlugdimensions(mat.get("sigma_y"), mat.get("sigma_ult"))[4])

for t in t:
    None

"""
Workflow:
First make sure the iteration works for a single material
Then run it for many materials
"""
