# Black
def nonmetal_nonmetal_dist0(coord_1, coord_2):
    
    flag_1 = coord_1[0] == coord_2[0] and coord_1[1] == coord_2[1]
    
    return flag_1


# Red
def nonmetal_nonmetal_dist1(coord_1, coord_2):

    flag_1 = coord_1[0] == ((coord_2[0] - 1) % 8) and coord_1[1] == ((coord_2[1] + 0) % 8)
    flag_2 = coord_1[0] == ((coord_2[0] + 1) % 8) and coord_1[1] == ((coord_2[1] + 0) % 8)
    flag_3 = coord_1[0] == ((coord_2[0] + 0) % 8) and coord_1[1] == ((coord_2[1] - 1) % 8)
    flag_4 = coord_1[0] == ((coord_2[0] + 0) % 8) and coord_1[1] == ((coord_2[1] + 1) % 8)
    flag_5 = coord_1[0] == ((coord_2[0] - 1) % 8) and coord_1[1] == ((coord_2[1] - 1) % 8)
    flag_6 = coord_1[0] == ((coord_2[0] + 1) % 8) and coord_1[1] == ((coord_2[1] + 1) % 8)
    
    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6


# Green
def nonmetal_nonmetal_dist2(coord_1, coord_2):

    flag_1 = coord_1[0] == ((coord_2[0] + 1) % 8) and coord_1[1] == ((coord_2[1] + 2) % 8)
    flag_2 = coord_1[0] == ((coord_2[0] - 1) % 8) and coord_1[1] == ((coord_2[1] + 1) % 8)
    flag_3 = coord_1[0] == ((coord_2[0] - 2) % 8) and coord_1[1] == ((coord_2[1] - 1) % 8)
    flag_4 = coord_1[0] == ((coord_2[0] - 1) % 8) and coord_1[1] == ((coord_2[1] - 2) % 8)
    flag_5 = coord_1[0] == ((coord_2[0] + 1) % 8) and coord_1[1] == ((coord_2[1] - 1) % 8)
    flag_6 = coord_1[0] == ((coord_2[0] + 2) % 8) and coord_1[1] == ((coord_2[1] + 1) % 8)
    
    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6


# Yellow
def nonmetal_nonmetal_dist3(coord_1, coord_2):

    flag_1 = coord_1[0] == ((coord_2[0] + 0) % 8) and coord_1[1] == ((coord_2[1] + 2) % 8)
    flag_2 = coord_1[0] == ((coord_2[0] - 2) % 8) and coord_1[1] == ((coord_2[1] + 0) % 8)
    flag_3 = coord_1[0] == ((coord_2[0] - 2) % 8) and coord_1[1] == ((coord_2[1] - 2) % 8)
    flag_4 = coord_1[0] == ((coord_2[0] + 0) % 8) and coord_1[1] == ((coord_2[1] - 2) % 8)
    flag_5 = coord_1[0] == ((coord_2[0] + 2) % 8) and coord_1[1] == ((coord_2[1] + 0) % 8)
    flag_6 = coord_1[0] == ((coord_2[0] + 2) % 8) and coord_1[1] == ((coord_2[1] + 2) % 8)
    
    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6


# Blue
def nonmetal_nonmetal_dist4(coord_1, coord_2):

    flag_1 = coord_1[0] == ((coord_2[0] - 1) % 8) and coord_1[1] == ((coord_2[1] + 2) % 8)
    flag_2 = coord_1[0] == ((coord_2[0] - 2) % 8) and coord_1[1] == ((coord_2[1] + 1) % 8)
    flag_3 = coord_1[0] == ((coord_2[0] - 3) % 8) and coord_1[1] == ((coord_2[1] - 1) % 8)
    flag_4 = coord_1[0] == ((coord_2[0] - 3) % 8) and coord_1[1] == ((coord_2[1] - 2) % 8)
    flag_5 = coord_1[0] == ((coord_2[0] - 1) % 8) and coord_1[1] == ((coord_2[1] - 3) % 8)
    flag_6 = coord_1[0] == ((coord_2[0] - 2) % 8) and coord_1[1] == ((coord_2[1] - 3) % 8)
    
    flag_7 = coord_1[0] == ((coord_2[0] + 2) % 8) and coord_1[1] == ((coord_2[1] - 1) % 8)
    flag_8 = coord_1[0] == ((coord_2[0] + 1) % 8) and coord_1[1] == ((coord_2[1] - 2) % 8)
    flag_9 = coord_1[0] == ((coord_2[0] + 3) % 8) and coord_1[1] == ((coord_2[1] + 1) % 8)
    flag_10 = coord_1[0] == ((coord_2[0] + 3) % 8) and coord_1[1] == ((coord_2[1] + 2) % 8)
    flag_11 = coord_1[0] == ((coord_2[0] + 1) % 8) and coord_1[1] == ((coord_2[1] + 3) % 8)
    flag_12 = coord_1[0] == ((coord_2[0] + 2) % 8) and coord_1[1] == ((coord_2[1] + 3) % 8)
    
    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6 or flag_7 or flag_8 or flag_9 or flag_10 or flag_11 or flag_12


# Purple
def nonmetal_nonmetal_dist5(coord_1, coord_2):

    flag_1 = coord_1[0] == ((coord_2[0] + 0) % 8) and coord_1[1] == ((coord_2[1] + 3) % 8)
    flag_2 = coord_1[0] == ((coord_2[0] - 3) % 8) and coord_1[1] == ((coord_2[1] + 0) % 8)
    flag_3 = coord_1[0] == ((coord_2[0] - 3) % 8) and coord_1[1] == ((coord_2[1] - 3) % 8)
    flag_4 = coord_1[0] == ((coord_2[0] + 0) % 8) and coord_1[1] == ((coord_2[1] - 3) % 8)
    flag_5 = coord_1[0] == ((coord_2[0] + 3) % 8) and coord_1[1] == ((coord_2[1] + 0) % 8)
    flag_6 = coord_1[0] == ((coord_2[0] + 3) % 8) and coord_1[1] == ((coord_2[1] + 3) % 8)
    
    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6


# Orange
def nonmetal_nonmetal_dist6(coord_1, coord_2):

    flag_1 = coord_1[0] == ((coord_2[0] + 4) % 8) and coord_1[1] == ((coord_2[1] + 3) % 8)
    flag_2 = coord_1[0] == ((coord_2[0] + 4) % 8) and coord_1[1] == ((coord_2[1] + 1) % 8)
    flag_3 = coord_1[0] == ((coord_2[0] + 4) % 8) and coord_1[1] == ((coord_2[1] - 1) % 8)
    flag_4 = coord_1[0] == ((coord_2[0] + 4) % 8) and coord_1[1] == ((coord_2[1] - 3) % 8)
    flag_5 = coord_1[0] == ((coord_2[0] + 3) % 8) and coord_1[1] == ((coord_2[1] - 1) % 8)
    flag_6 = coord_1[0] == ((coord_2[0] + 3) % 8) and coord_1[1] == ((coord_2[1] - 4) % 8)
    
    flag_7 = coord_1[0] == ((coord_2[0] + 1) % 8) and coord_1[1] == ((coord_2[1] - 3) % 8)
    flag_8 = coord_1[0] == ((coord_2[0] + 1) % 8) and coord_1[1] == ((coord_2[1] - 4) % 8)
    flag_9 = coord_1[0] == ((coord_2[0] - 1) % 8) and coord_1[1] == ((coord_2[1] + 3) % 8)
    flag_10 = coord_1[0] == ((coord_2[0] - 1) % 8) and coord_1[1] == ((coord_2[1] - 4) % 8)
    flag_11 = coord_1[0] == ((coord_2[0] - 3) % 8) and coord_1[1] == ((coord_2[1] + 1) % 8)
    flag_12 = coord_1[0] == ((coord_2[0] - 3) % 8) and coord_1[1] == ((coord_2[1] - 4) % 8)
    
    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6 or flag_7 or flag_8 or flag_9 or flag_10 or flag_11 or flag_12


# Pink
def nonmetal_nonmetal_dist7(coord_1, coord_2):

    flag_1 = coord_1[0] == ((coord_2[0] + 4) % 8) and coord_1[1] == ((coord_2[1] + 2) % 8)
    flag_2 = coord_1[0] == ((coord_2[0] + 4) % 8) and coord_1[1] == ((coord_2[1] - 2) % 8)
    flag_3 = coord_1[0] == ((coord_2[0] + 2) % 8) and coord_1[1] == ((coord_2[1] - 2) % 8)
    flag_4 = coord_1[0] == ((coord_2[0] + 2) % 8) and coord_1[1] == ((coord_2[1] - 4) % 8)
    flag_5 = coord_1[0] == ((coord_2[0] - 2) % 8) and coord_1[1] == ((coord_2[1] + 2) % 8)
    flag_6 = coord_1[0] == ((coord_2[0] - 2) % 8) and coord_1[1] == ((coord_2[1] - 4) % 8)
    
    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6


# Gray
def nonmetal_nonmetal_dist8(coord_1, coord_2):

    flag_1 = coord_1[0] == ((coord_2[0] + 4) % 8) and coord_1[1] == ((coord_2[1] + 0) % 8)
    flag_2 = coord_1[0] == ((coord_2[0] + 4) % 8) and coord_1[1] == ((coord_2[1] - 4) % 8)
    flag_3 = coord_1[0] == ((coord_2[0] + 0) % 8) and coord_1[1] == ((coord_2[1] - 4) % 8)
    
    return flag_1 or flag_2 or flag_3


# Turquoise
def nonmetal_nonmetal_dist9(coord_1, coord_2):

    flag_1 = coord_1[0] == ((coord_2[0] + 3) % 8) and coord_1[1] == ((coord_2[1] - 2) % 8)
    flag_2 = coord_1[0] == ((coord_2[0] + 3) % 8) and coord_1[1] == ((coord_2[1] - 3) % 8)
    flag_3 = coord_1[0] == ((coord_2[0] + 2) % 8) and coord_1[1] == ((coord_2[1] - 3) % 8)
    flag_4 = coord_1[0] == ((coord_2[0] - 2) % 8) and coord_1[1] == ((coord_2[1] + 3) % 8)
    flag_5 = coord_1[0] == ((coord_2[0] - 3) % 8) and coord_1[1] == ((coord_2[1] + 3) % 8)
    flag_6 = coord_1[0] == ((coord_2[0] - 3) % 8) and coord_1[1] == ((coord_2[1] + 2) % 8)
    
    return flag_1 or flag_2 or flag_3 or flag_4 or flag_5 or flag_6



# Relative position of two non-metals
def nonmetal_nonmetal_pos(coord_1, coord_2):
    
    
    if nonmetal_nonmetal_dist0(coord_1, coord_2):
        return 0
    
    if nonmetal_nonmetal_dist1(coord_1, coord_2):
        return 1
    
    if nonmetal_nonmetal_dist2(coord_1, coord_2):
        return 2
    
    if nonmetal_nonmetal_dist3(coord_1, coord_2):
        return 3
    
    if nonmetal_nonmetal_dist4(coord_1, coord_2):
        return 4
    
    if nonmetal_nonmetal_dist5(coord_1, coord_2):
        return 5
    
    if nonmetal_nonmetal_dist6(coord_1, coord_2):
        return 6
    
    if nonmetal_nonmetal_dist7(coord_1, coord_2):
        return 7
    
    if nonmetal_nonmetal_dist8(coord_1, coord_2):
        return 8
    
    if nonmetal_nonmetal_dist9(coord_1, coord_2):
        return 9
    
    else:
        raise Exception("Incorrect point position")
    