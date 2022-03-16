import json
from pathlib import Path
from pymatgen.core import Structure
import numpy as np


# Read data in pymatgen format
def read_pymatgen_struct(filename):
    with open(filename, 'r') as file:
        json_dict = json.load(file)
    return Structure.from_dict(json_dict)


# Extract all the data in pymatgen format
def get_structs(dataset_path):
    
    dataset_path = Path(dataset_path)

    structs = {
        item.name : read_pymatgen_struct(item)
        for item in (dataset_path / "structures").iterdir()
    }
    return structs


# Get simplified data format: list of tuples (element, grid coordinates)
def get_view(struct):
    view = []
    for element in struct:
        element_name = element.species.elements[0].name
        element_frac_coord = (element.frac_coords * 8).astype(int)
        view.append((element_name, element_frac_coord))
    return view


# Obtaining lattice defects relative to the base lattice Mo64 S128
def get_defects(struct_view, base_struct_view):
    
    w_substitution = []
    se_substitution = []
    mo_skipped = []
    s_skipped = []
    
    struct_idx, base_idx = 0, 0
    while base_idx != 64:
        
        if struct_view[struct_idx][0] == 'Mo' and (struct_view[struct_idx][1] != base_struct_view[base_idx][1]).any():
            mo_skipped.append(base_struct_view[base_idx][1])
            base_idx += 1
        
        elif struct_view[struct_idx][0] != 'Mo' and struct_view[struct_idx][0] != 'W':
            mo_skipped.append(base_struct_view[base_idx][1])
            base_idx += 1
       
        elif struct_view[struct_idx][0] == 'W':
            w_substitution.append(struct_view[struct_idx]) # фиксил
            struct_idx += 1
            base_idx += 1
            
        else: 
            struct_idx += 1
            base_idx += 1
            
    while struct_view[struct_idx][0] == 'W':
        for i in range(len(mo_skipped)):
            if (mo_skipped[i] == struct_view[struct_idx][1]).all():
                mo_skipped.pop(i)
                break
        w_substitution.append(struct_view[struct_idx])
        struct_idx += 1
        
    while base_idx != 192:
        
        if struct_idx >= len(struct_view):
            s_skipped.append(base_struct_view[base_idx][1])
            base_idx += 1 
            
        elif struct_view[struct_idx][0] == 'S' and (struct_view[struct_idx][1] != base_struct_view[base_idx][1]).any():
            s_skipped.append(base_struct_view[base_idx][1])
            base_idx += 1  
    
        elif struct_view[struct_idx][0] == 'Se':
            se_substitution.append(struct_view[struct_idx])
            struct_idx += 1
            
        else:
            struct_idx += 1
            base_idx += 1
    
    for defect in se_substitution:
        for i in range(len(s_skipped)):
            if (s_skipped[i] == defect[1]).all():
                s_skipped.pop(i)
                break
    
    for i in range(len(mo_skipped)):
        mo_skipped[i] = ('Mo', mo_skipped[i])
        
    for i in range(len(s_skipped)):
        s_skipped[i] = ('S', s_skipped[i])
    
    # return a set of defects (Mo, W, S, Se)
    return mo_skipped + w_substitution + s_skipped + se_substitution


# Get defects count/types
def get_defect_counts(defects):
    mo, w, se, s = 0, 0, 0, 0
    for record in defects:
        if record[0] == 'Mo':
            mo += 1
        elif record[0] == 'W':
            w += 1
        elif record[0] == 'S':
            s += 1
        elif record[0] == 'Se':
            se += 1

    #return { 'Mo': mo, 'W': w, 'S': s, 'Se': se, 'All': mo+w+s+se }
    return (mo, w, s, se, mo+w+se+s)


# Get all data in new format
def to_new_format(structs, base_struct):
    
    structs_views = list(map(get_view, structs.values()))
    base_struct_view = get_view(base_struct)

    defects = []
    for struct_view in structs_views:
        defects.append(get_defects(struct_view, base_struct_view))
        
    new_format_structs = dict(zip(structs.keys(), defects))
    return new_format_structs


# filter objects by defects set
def filter_by_defects(structs, defects, targets=None):
    
    defect_counts = list(map(get_defect_counts, structs.values()))
    
    correct_keys = list(filter(lambda x: x[1] == defects, list(zip(structs.keys(), defect_counts))))
    correct_keys = list(zip(*correct_keys))[0]
    
    correct_structs = { key : structs[key] for key in correct_keys }
    
    if targets is not None:
        correct_indices = list(map(lambda x: x.rstrip('.json'), correct_keys))
        correct_targets = targets.loc[correct_indices]
        return correct_structs, correct_targets
    
    return correct_structs
