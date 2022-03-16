from metal_nonmetal_pos import *
from nonmetal_nonmetal_pos import *


# Non-metals are on one side of the metal layer (True - yes, False - no)
def nonmetals_same_side(coord_1, coord_2):
    
    return coord_1[2] == coord_2[2]