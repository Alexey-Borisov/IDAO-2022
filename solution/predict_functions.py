import catboost as cat
import pandas as pd
import numpy as np


from utils_features import metal_nonmetal_pos, nonmetal_nonmetal_pos, nonmetals_same_side
from utils_preprocess import get_defect_counts
from collections import defaultdict


# Mo, W, S, Se - defects order in description

# below are the functions for prediction on each of the categories of defects

def predict_band_gap_1002(private_structs, public_structs, targets): 
    
    def generate_features_1002(struct):
        
        mo_coord = struct[0][1]
        se1_coord = struct[1][1]
        se2_coord = struct[2][1]
        
        mo_pos_1 = metal_nonmetal_pos(mo_coord, se1_coord)
        mo_pos_2 = metal_nonmetal_pos(mo_coord, se2_coord)
        same_side = nonmetals_same_side(se1_coord, se2_coord)
        se_pos = nonmetal_nonmetal_pos(se1_coord, se2_coord)
        
        return np.array([min(mo_pos_1, mo_pos_2), max(mo_pos_1, mo_pos_2)])#, same_side, se_pos])
    
    targets_ids = list(map(lambda x: x.rstrip('.json'), public_structs.keys()))
    targets_part = targets.loc[targets_ids]
    
    X_train = np.array(list(map(generate_features_1002, public_structs.values())))
    X_test = np.array(list(map(generate_features_1002, private_structs.values())))
    y_train = np.array(targets_part).ravel()
    
    bst = cat.CatBoostRegressor()
    bst.fit(X_train, y_train, silent=True)
    y_pred = bst.predict(X_test)
    
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets
    
        
def predict_band_gap_0111(private_structs, public_structs, targets): 
    
    def generate_features_0111(struct):
        
        w_coord = struct[0][1]
        s_coord = struct[1][1]
        se_coord = struct[2][1]
        
        w_se_pos = metal_nonmetal_pos(w_coord, se_coord)
        w_s_pos = metal_nonmetal_pos(w_coord, s_coord)
        same_side = nonmetals_same_side(se_coord, s_coord)
        s_se_pos = nonmetal_nonmetal_pos(se_coord, s_coord)
        
        return np.array([w_se_pos, w_s_pos, same_side, s_se_pos])
    
    targets_ids = list(map(lambda x: x.rstrip('.json'), public_structs.keys()))
    targets_part = targets.loc[targets_ids]
    
    X_train = np.array(list(map(generate_features_0111, public_structs.values())))
    X_test = np.array(list(map(generate_features_0111, private_structs.values())))
    y_train = np.array(targets_part).ravel()
    
    bst = cat.CatBoostRegressor()
    bst.fit(X_train, y_train, silent=True)
    y_pred = bst.predict(X_test)
    
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets

    
def predict_band_gap_0102(private_structs, public_structs, targets): 
    
    targets_ids = list(map(lambda x: x.rstrip('.json'), public_structs.keys()))
    targets_part = targets.loc[targets_ids]
    
    y_pred = np.full(len(private_structs), targets_part.mean())
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets
    

def predict_band_gap_0120(private_structs, public_structs, targets): 
    
    def generate_features_0120(struct):
        
        w_coord = struct[0][1]
        s1_coord = struct[1][1]
        s2_coord = struct[2][1]
        
        w_pos_1 = metal_nonmetal_pos(w_coord, s1_coord)
        w_pos_2 = metal_nonmetal_pos(w_coord, s2_coord)
        same_side = nonmetals_same_side(s1_coord, s2_coord)
        s_pos = nonmetal_nonmetal_pos(s1_coord, s2_coord)
        
        return np.array([min(w_pos_1, w_pos_2), max(w_pos_1, w_pos_2), same_side, s_pos])
    
    targets_ids = list(map(lambda x: x.rstrip('.json'), public_structs.keys()))
    targets_part = targets.loc[targets_ids]
    
    X_train = np.array(list(map(generate_features_0120, public_structs.values())))
    X_test = np.array(list(map(generate_features_0120, private_structs.values())))
    y_train = np.array(targets_part).ravel()
    
    bst = cat.CatBoostRegressor()
    bst.fit(X_train, y_train, silent=True)
    y_pred = bst.predict(X_test)
    
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets



def predict_band_gap_1011(private_structs, public_structs, targets): 
    
    def generate_features_1011(struct):
        
        mo_coord = struct[0][1]
        s_coord = struct[1][1]
        se_coord = struct[2][1]
        
        mo_se_pos = metal_nonmetal_pos(mo_coord, se_coord)
        mo_s_pos = metal_nonmetal_pos(mo_coord, s_coord)
        same_side = nonmetals_same_side(se_coord, s_coord)
        s_se_pos = nonmetal_nonmetal_pos(se_coord, s_coord)
        
        return np.array([mo_se_pos, mo_s_pos])#, same_side, s_se_pos])
    
    targets_ids = list(map(lambda x: x.rstrip('.json'), public_structs.keys()))
    targets_part = targets.loc[targets_ids]
    
    X_train = np.array(list(map(generate_features_1011, public_structs.values())))
    X_test = np.array(list(map(generate_features_1011, private_structs.values())))
    y_train = np.array(targets_part).ravel()
    
    bst = cat.CatBoostRegressor()
    bst.fit(X_train, y_train, silent=True)
    y_pred = bst.predict(X_test)
    
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets


def predict_band_gap_1020(private_structs, public_structs, targets): 
    
    def generate_features_1020(struct):
        
        mo_coord = struct[0][1]
        s1_coord = struct[1][1]
        s2_coord = struct[2][1]
        
        mo_pos_1 = metal_nonmetal_pos(mo_coord, s1_coord)
        mo_pos_2 = metal_nonmetal_pos(mo_coord, s2_coord)
        same_side = nonmetals_same_side(s1_coord, s2_coord)
        s_pos = nonmetal_nonmetal_pos(s1_coord, s2_coord)
        
        return np.array([min(mo_pos_1, mo_pos_2), max(mo_pos_1, mo_pos_2)])#, same_side, s_pos])
    
    targets_ids = list(map(lambda x: x.rstrip('.json'), public_structs.keys()))
    targets_part = targets.loc[targets_ids]
    
    X_train = np.array(list(map(generate_features_1020, public_structs.values())))
    X_test = np.array(list(map(generate_features_1020, private_structs.values())))
    y_train = np.array(targets_part).ravel()
    
    bst = cat.CatBoostRegressor()
    bst.fit(X_train, y_train, silent=True)
    y_pred = bst.predict(X_test)
    
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets


def predict_band_gap_0002(private_structs, public_structs, targets): 
    
    targets_ids = list(map(lambda x: x.rstrip('.json'), public_structs.keys()))
    targets_part = targets.loc[targets_ids]
    
    y_pred = np.full(len(private_structs), targets_part.mean())
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets


def predict_band_gap_0020(private_structs, public_structs, targets): 
    
    def generate_features_0020(struct):
        
        se1_coord = struct[0][1]
        se2_coord = struct[1][1]
        
        same_side = nonmetals_same_side(se1_coord, se2_coord)
        se_pos = nonmetal_nonmetal_pos(se1_coord, se2_coord)
        
        return np.array([same_side, se_pos])
    
    targets_ids = list(map(lambda x: x.rstrip('.json'), public_structs.keys()))
    targets_part = targets.loc[targets_ids]
    
    X_train = np.array(list(map(generate_features_0020, public_structs.values())))
    X_test = np.array(list(map(generate_features_0020, private_structs.values())))
    y_train = np.array(targets_part).ravel()
    
    bst = cat.CatBoostRegressor()
    bst.fit(X_train, y_train, silent=True)
    y_pred = bst.predict(X_test)
    
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets


def predict_band_gap_0011(private_structs, public_structs, targets): 
    
    def generate_features_0011(struct):
        
        s_coord = struct[0][1]
        se_coord = struct[1][1]
        
        same_side = nonmetals_same_side(s_coord, se_coord)
        s_se_pos = nonmetal_nonmetal_pos(s_coord, se_coord)
        
        return np.array([same_side, s_se_pos])
    
    targets_ids = list(map(lambda x: x.rstrip('.json'), public_structs.keys()))
    targets_part = targets.loc[targets_ids]
    
    X_train = np.array(list(map(generate_features_0011, public_structs.values())))
    X_test = np.array(list(map(generate_features_0011, private_structs.values())))
    y_train = np.array(targets_part).ravel()
    
    bst = cat.CatBoostRegressor()
    bst.fit(X_train, y_train, silent=True)
    y_pred = bst.predict(X_test)
    
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets


def predict_band_gap_1001(private_structs, public_structs, targets): 
    
    def generate_features_1001(struct):
        
        mo_coord = struct[0][1]
        se_coord = struct[1][1]
        
        mo_pos = metal_nonmetal_pos(mo_coord, se_coord)
        
        return np.array([mo_pos])
    
    targets_ids = list(map(lambda x: x.rstrip('.json'), public_structs.keys()))
    targets_part = targets.loc[targets_ids]
    
    X_train = np.array(list(map(generate_features_1001, public_structs.values())))
    X_test = np.array(list(map(generate_features_1001, private_structs.values())))
    y_train = np.array(targets_part).ravel()
    
    bst = cat.CatBoostRegressor()
    bst.fit(X_train, y_train, silent=True)
    y_pred = bst.predict(X_test)
    
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets


def predict_band_gap_1010(private_structs, public_structs, targets): 
    
    def generate_features_1010(struct):
        
        mo_coord = struct[0][1]
        s_coord = struct[1][1]
        
        mo_pos = metal_nonmetal_pos(mo_coord, s_coord)
        
        return np.array([mo_pos])
    
    targets_ids = list(map(lambda x: x.rstrip('.json'), public_structs.keys()))
    targets_part = targets.loc[targets_ids]
    
    X_train = np.array(list(map(generate_features_1010, public_structs.values())))
    X_test = np.array(list(map(generate_features_1010, private_structs.values())))
    y_train = np.array(targets_part).ravel()
    
    bst = cat.CatBoostRegressor()
    bst.fit(X_train, y_train, silent=True)
    y_pred = bst.predict(X_test)
    
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets


def predict_band_gap_0101(private_structs, public_structs, targets): 
    
    targets_ids = list(map(lambda x: x.rstrip('.json'), public_structs.keys()))
    targets_part = targets.loc[targets_ids]
    
    y_pred = np.full(len(private_structs), targets_part.mean())
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets


def predict_band_gap_0110(private_structs, public_structs, targets): 
    
    def generate_features_0110(struct):
        
        w_coord = struct[0][1]
        s_coord = struct[1][1]
        
        w_pos = metal_nonmetal_pos(w_coord, s_coord)
        
        return np.array([w_pos])
    
    targets_ids = list(map(lambda x: x.rstrip('.json'), public_structs.keys()))
    targets_part = targets.loc[targets_ids]
    
    X_train = np.array(list(map(generate_features_0110, public_structs.values())))
    X_test = np.array(list(map(generate_features_0110, private_structs.values())))
    y_train = np.array(targets_part).ravel()
    
    bst = cat.CatBoostRegressor()
    bst.fit(X_train, y_train, silent=True)
    y_pred = bst.predict(X_test)
    
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets


def predict_band_gap_0010(private_structs, public_structs, targets): 
    
    y_pred = np.full(len(private_structs), 1.145457142857143) # mean target from train part with (0, 1, 1, 0)
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets


def predict_band_gap_0001(private_structs, public_structs, targets): 
    
    y_pred = np.full(len(private_structs), 1.80258) # mean target from train part with (0, 1, 0, 1)
    predicted_targets = pd.DataFrame({ 'band_gap' : y_pred }, index=list(map(lambda x: x.rstrip('.json'), private_structs.keys())))
    return predicted_targets


# A function that applies the necessary prediction function for each object
def predict_band_gap(public_structs, private_structs, targets):
    
    # group by set of defects
    public_groups = defaultdict(dict)
    private_groups = defaultdict(dict)
    
    for key, value in public_structs.items():    
        elem_defects = get_defect_counts(value)
        public_groups[elem_defects].update({key : value})
        
    for key, value in private_structs.items():    
        elem_defects = get_defect_counts(value)
        private_groups[elem_defects].update({key : value})
        
    # for each group separately predict the value
    predictions = dict()
    for key in private_groups.keys():
        
        if key == (1, 0, 0, 2, 3):
            predicted_target = predict_band_gap_1002(private_groups[key], public_groups[key], targets)
            
        if key == (0, 1, 1, 1, 3):
            predicted_target = predict_band_gap_0111(private_groups[key], public_groups[key], targets)
            
        if key == (0, 1, 0, 2, 3):
            predicted_target = predict_band_gap_0102(private_groups[key], public_groups[key], targets)
            
        if key == (0, 1, 2, 0, 3):
            predicted_target = predict_band_gap_0120(private_groups[key], public_groups[key], targets)
            
        if key == (1, 0, 1, 1, 3):
            predicted_target = predict_band_gap_1011(private_groups[key], public_groups[key], targets)
            
        if key == (1, 0, 2, 0, 3):
            predicted_target = predict_band_gap_1020(private_groups[key], public_groups[key], targets)
            
        if key == (0, 0, 0, 2, 2):
            predicted_target = predict_band_gap_0002(private_groups[key], public_groups[key], targets)
            
        if key == (0, 0, 2, 0, 2):
            predicted_target = predict_band_gap_0020(private_groups[key], public_groups[key], targets)
            
        if key == (0, 0, 1, 1, 2):
            predicted_target = predict_band_gap_0011(private_groups[key], public_groups[key], targets)
            
        if key == (1, 0, 0, 1, 2):
            predicted_target = predict_band_gap_1001(private_groups[key], public_groups[key], targets)
            
        if key == (1, 0, 1, 0, 2):
            predicted_target = predict_band_gap_1010(private_groups[key], public_groups[key], targets)
            
        if key == (0, 1, 0, 1, 2):
            predicted_target = predict_band_gap_0101(private_groups[key], public_groups[key], targets)
            
        if key == (0, 1, 1, 0, 2):
            predicted_target = predict_band_gap_0110(private_groups[key], public_groups[key], targets)
            
        if key == (0, 0, 1, 0, 1):
            predicted_target = predict_band_gap_0010(private_groups[key], public_groups[key], targets)
            
        if key == (0, 0, 0, 1, 1):
            predicted_target = predict_band_gap_0001(private_groups[key], public_groups[key], targets)
            
        predictions[key] = predicted_target

    return predictions


# Getting answer as pd.DataFrame
def get_submission(answer):
    submission = pd.DataFrame()
    for value in answer.values():
        submission = pd.concat((submission, value), axis=0)
    submission.rename(columns={'band_gap' : 'predictions'}, inplace=True)
    return submission
    