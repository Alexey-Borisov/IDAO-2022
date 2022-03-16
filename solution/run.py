import pandas as pd


from utils_preprocess import to_new_format, get_structs, read_pymatgen_struct
from predict_functions import predict_band_gap, get_submission


if __name__ == "__main__":
    
    # data paths
    path_to_data = "./data"
    public_folder = "dichalcogenides_public"
    private_folder = "dichalcogenides_private"
    base_struct_filename = "base_struct.json"
    targets_filename = "targets.csv"
    
    # extract data
    public_structs = get_structs(path_to_data + "/" + public_folder)
    private_structs = get_structs(path_to_data + "/" + private_folder)
    base_struct = read_pymatgen_struct(base_struct_filename)
    targets = pd.read_csv(path_to_data + "/" + public_folder + "/" + targets_filename, index_col=0)
    
    # bring data to a new format (list of defects)
    public_structs = to_new_format(public_structs, base_struct)
    private_structs = to_new_format(private_structs, base_struct)
    
    # get the answer: a dictionary, each element of which corresponds to the answer to
    # one of the categories (for a simple quality check on individual categories)
    answer = predict_band_gap(public_structs, private_structs, targets)
    
    # get the answer in the form of pd.DataFrame
    submission = get_submission(answer)

    # create the necessary answer file
    submission.to_csv("submission.csv", index_label='id')
