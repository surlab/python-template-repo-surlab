# +
from src import config as cfg
import os
#import scipy.io as sio
#import h5py
import json
#from datetime import datetime as dt
################
# data in
#################
def readfile(path):
    print(f'Reading file at {path}')
    with open(path, 'r') as f:
        lines = f.read()
        print(lines)
def loadmat(path):
    try:
        f = _loadmat(path)
    except NotImplementedError as E:
        f = h5py.File(path,'r')
    if 'soma_cell' in f.keys():
        return f['soma_cell']
    elif 'dend_cell' in f.keys():
        pass
        #return f['dend_cell']
    return f
def _check_keys( dict):
    """
    checks if entries in dictionary are mat-objects. If yes
    todict is called to change them to nested dictionaries
    """
    for key in dict:
        if isinstance(dict[key], sio.matlab.mio5_params.mat_struct):
            dict[key] = _todict(dict[key])
    return dict
def _todict(matobj):
    """
    A recursive function which constructs from matobjects nested dictionaries
    """
    dict = {}
    for strg in matobj._fieldnames:
        elem = matobj.__dict__[strg]
        if isinstance(elem, sio.matlab.mio5_params.mat_struct):
            dict[strg] = _todict(elem)
        else:
            dict[strg] = elem
    return dict
def _loadmat(filename):
    """
    this function should be called instead of direct scipy.io .loadmat
    as it cures the problem of not properly recovering python dictionaries
    from mat files. It calls the function check keys to cure all entries
    which are still mat-objects
    """
    data = sio.loadmat(filename, struct_as_record=False, squeeze_me=True)
    return _check_keys(data)
################
# data out
#################
def save_named_iterable_to_json(**kwargs):
    for key, value in kwargs.items():
        timestamp = dt.now().strftime("%Y%m%d_%H%M%S")
        file_name = key +'_' + timestamp + ".json"
        summary_path = os.path.join(cfg.collect_summary_at_path, "summary_plots")
        file_path = os.path.join(summary_path, file_name)
        if not (os.path.isdir(summary_path)):
            os.makedirs(summary_path)
        with open(file_path, "w") as f:
            json.dump(value, f, indent=4)
def save_csv(df, name_keywords=''):
    dfname = f'{name_keywords}.csv'
    df_path = os.path.join(cfg.collect_summary_at_path, dfname)
    print(f'Saving dataframe to {df_path}')
    df.to_csv(df_path)
def save_plot(fig, current_data_dir):
    # save it local with the other data
    file_name = "annotated_dendrite.svg"
    file_dir = os.path.join(current_data_dir, cfg.subfolder_name)
    if not (os.path.isdir(file_dir)):
        os.mkdir(file_dir)
    file_path = os.path.join(current_data_dir, cfg.subfolder_name, file_name)
    fig.savefig(file_path)
    if cfg.collect_summary_at_path:
        cell_dir, FOV_name = os.path.split(current_data_dir)
        _, cell_name = os.path.split(cell_dir)
        file_name = cell_name + "_" + FOV_name + "_annotated_dendrite.svg"
        if not (os.path.isdir(cfg.collect_summary_at_path)):
            os.mkdir(cfg.collect_summary_at_path)
        file_path = os.path.join(cfg.collect_summary_at_path, file_name)
        fig.savefig(file_path)
