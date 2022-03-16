# Red
def metal_nonmetal_dist1(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == ((coord_nonmetal[0] + 1) % 8) and coord_metal[1] == coord_nonmetal[1]
    flag_2 = coord_metal[0] == coord_nonmetal[0] and coord_metal[1] == coord_nonmetal[1]
    flag_3 = coord_metal[0] == coord_nonmetal[0] and coord_metal[1] == ((coord_nonmetal[1] - 1) % 8)
    
    return flag_1 or flag_2 or flag_3


# Yellow
def metal_nonmetal_dist2(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == ((coord_nonmetal[0] + 1) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 1) % 8)
    flag_2 = coord_metal[0] == ((coord_nonmetal[0] + 1) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 1) % 8)
    flag_3 = coord_metal[0] == ((coord_nonmetal[0] - 1) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 1) % 8)

    return flag_1 or flag_2 or flag_3

# Green
def metal_nonmetal_dist3(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == coord_nonmetal[0] and coord_metal[1] == ((coord_nonmetal[1] + 1) % 8)
    flag_2 = coord_metal[0] == ((coord_nonmetal[0] - 1) % 8) and coord_metal[1] == coord_nonmetal[1]
    flag_3 = coord_metal[0] == coord_nonmetal[0] and coord_metal[1] == ((coord_nonmetal[1] - 2) % 8)
    
    flag_4 = coord_metal[0] == ((coord_nonmetal[0] - 1) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 2) % 8)
    flag_5 = coord_metal[0] == ((coord_nonmetal[0] + 2) % 8) and coord_metal[1] == coord_nonmetal[1]
    flag_6 = coord_metal[0] == ((coord_nonmetal[0] + 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 1) % 8)
    
    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6


# Blue
def metal_nonmetal_dist4(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == ((coord_nonmetal[0] + 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 2) % 8)
    flag_2 = coord_metal[0] == ((coord_nonmetal[0] + 1) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 2) % 8)
    flag_3 = coord_metal[0] == ((coord_nonmetal[0] - 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 1) % 8)
    
    flag_4 = coord_metal[0] == ((coord_nonmetal[0] - 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 2) % 8)
    flag_5 = coord_metal[0] == ((coord_nonmetal[0] + 1) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 2) % 8)
    flag_6 = coord_metal[0] == ((coord_nonmetal[0] + 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 1) % 8)

    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6


# Light blue
def metal_nonmetal_dist5(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == ((coord_nonmetal[0] + 0) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 2) % 8)
    flag_2 = coord_metal[0] == ((coord_nonmetal[0] - 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 0) % 8)
    flag_3 = coord_metal[0] == ((coord_nonmetal[0] - 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 3) % 8)
    
    flag_4 = coord_metal[0] == ((coord_nonmetal[0] + 0) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 3) % 8)
    flag_5 = coord_metal[0] == ((coord_nonmetal[0] + 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 0) % 8)
    flag_6 = coord_metal[0] == ((coord_nonmetal[0] + 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 2) % 8)

    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6


# Purple
def metal_nonmetal_dist6(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == ((coord_nonmetal[0] - 1) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 1) % 8)
    flag_2 = coord_metal[0] == ((coord_nonmetal[0] - 1) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 3) % 8)
    flag_3 = coord_metal[0] == ((coord_nonmetal[0] + 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 1) % 8)

    return flag_1 or flag_2 or flag_3


# Gray
def metal_nonmetal_dist7(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == ((coord_nonmetal[0] - 1) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 2) % 8)
    flag_2 = coord_metal[0] == ((coord_nonmetal[0] - 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 1) % 8)
    flag_3 = coord_metal[0] == ((coord_nonmetal[0] - 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 4) % 8)
    
    flag_4 = coord_metal[0] == ((coord_nonmetal[0] - 1) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 4) % 8)
    flag_5 = coord_metal[0] == ((coord_nonmetal[0] + 4) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 1) % 8)
    flag_6 = coord_metal[0] == ((coord_nonmetal[0] + 4) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 2) % 8)

    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6


# Pink
def metal_nonmetal_dist8(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == ((coord_nonmetal[0] + 0) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 3) % 8)
    flag_2 = coord_metal[0] == ((coord_nonmetal[0] - 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 0) % 8)
    flag_3 = coord_metal[0] == ((coord_nonmetal[0] - 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 4) % 8)
    
    flag_4 = coord_metal[0] == ((coord_nonmetal[0] + 0) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 4) % 8)
    flag_5 = coord_metal[0] == ((coord_nonmetal[0] + 4) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 0) % 8)
    flag_6 = coord_metal[0] == ((coord_nonmetal[0] + 4) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 3) % 8)

    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6


# Burgundy
def metal_nonmetal_dist9(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == ((coord_nonmetal[0] + 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 3) % 8)
    flag_2 = coord_metal[0] == ((coord_nonmetal[0] + 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 2) % 8)
    flag_3 = coord_metal[0] == ((coord_nonmetal[0] - 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 2) % 8)

    return flag_1 or flag_2 or flag_3


# Brown
def metal_nonmetal_dist10(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == ((coord_nonmetal[0] + 1) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 3) % 8)
    flag_2 = coord_metal[0] == ((coord_nonmetal[0] + 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 3) % 8)
    flag_3 = coord_metal[0] == ((coord_nonmetal[0] - 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 1) % 8)
    
    flag_4 = coord_metal[0] == ((coord_nonmetal[0] - 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 3) % 8)
    flag_5 = coord_metal[0] == ((coord_nonmetal[0] + 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 1) % 8)
    flag_6 = coord_metal[0] == ((coord_nonmetal[0] + 1) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 3) % 8)

    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6


# Crimson
def metal_nonmetal_dist11(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == ((coord_nonmetal[0] - 1) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 3) % 8)
    flag_2 = coord_metal[0] == ((coord_nonmetal[0] - 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 1) % 8)
    flag_3 = coord_metal[0] == ((coord_nonmetal[0] - 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 3) % 8)

    return flag_1 or flag_2 or flag_3


# Beige
def metal_nonmetal_dist12(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == ((coord_nonmetal[0] - 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 3) % 8)
    flag_2 = coord_metal[0] == ((coord_nonmetal[0] - 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 2) % 8)
    flag_3 = coord_metal[0] == ((coord_nonmetal[0] - 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] + 2) % 8)

    return flag_1 or flag_2 or flag_3


# Dark green
def metal_nonmetal_dist13(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == ((coord_nonmetal[0] + 4) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 1) % 8)
    flag_2 = coord_metal[0] == ((coord_nonmetal[0] + 4) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 4) % 8)
    flag_3 = coord_metal[0] == ((coord_nonmetal[0] + 1) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 4) % 8)

    return flag_1 or flag_2 or flag_3


# Light green
def metal_nonmetal_dist14(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == ((coord_nonmetal[0] + 4) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 2) % 8)
    flag_2 = coord_metal[0] == ((coord_nonmetal[0] + 4) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 3) % 8)
    flag_3 = coord_metal[0] == ((coord_nonmetal[0] + 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 2) % 8)
    
    flag_4 = coord_metal[0] == ((coord_nonmetal[0] + 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 4) % 8)
    flag_5 = coord_metal[0] == ((coord_nonmetal[0] + 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 3) % 8)
    flag_6 = coord_metal[0] == ((coord_nonmetal[0] + 2) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 4) % 8)

    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6


# Lilac
def metal_nonmetal_dist15(coord_metal, coord_nonmetal):
    
    flag_1 = coord_metal[0] == ((coord_nonmetal[0] + 3) % 8) and coord_metal[1] == ((coord_nonmetal[1] - 3) % 8)

    return flag_1
        

# Relative position of metal and non-metal
def metal_nonmetal_pos(coord_metal, coord_nonmetal):
    
    if metal_nonmetal_dist1(coord_metal, coord_nonmetal):
        return 1
    
    if metal_nonmetal_dist2(coord_metal, coord_nonmetal):
        return 2
    
    if metal_nonmetal_dist3(coord_metal, coord_nonmetal):
        return 3
    
    if metal_nonmetal_dist4(coord_metal, coord_nonmetal):
        return 4
    
    if metal_nonmetal_dist5(coord_metal, coord_nonmetal):
        return 5
    
    if metal_nonmetal_dist6(coord_metal, coord_nonmetal):
        return 6
    
    if metal_nonmetal_dist7(coord_metal, coord_nonmetal):
        return 7
    
    if metal_nonmetal_dist8(coord_metal, coord_nonmetal):
        return 8
    
    if metal_nonmetal_dist9(coord_metal, coord_nonmetal):
        return 9
    
    if metal_nonmetal_dist10(coord_metal, coord_nonmetal):
        return 10
    
    if metal_nonmetal_dist11(coord_metal, coord_nonmetal):
        return 11
    
    if metal_nonmetal_dist12(coord_metal, coord_nonmetal):
        return 12
    
    if metal_nonmetal_dist13(coord_metal, coord_nonmetal):
        return 13
    
    if metal_nonmetal_dist14(coord_metal, coord_nonmetal):
        return 14
    
    if metal_nonmetal_dist15(coord_metal, coord_nonmetal):
        return 15
    
    else:
        raise Exception("Incorrect point position")
