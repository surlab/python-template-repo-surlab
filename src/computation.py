import numpy as np
from src import config as cfg
from src import helper_functions as hf
import xarray as xr
#####################################
def select_timesteps(traces, first_sample =cfg.first_sample_to_take, last_sample =cfg.last_sample_to_take):
    selected_timesteps = traces[:,:,first_sample:last_sample]
    return selected_timesteps
def get_stim_on_traces(traces):
    return select_timesteps(traces, first_sample =cfg.stim_start, last_sample =cfg.stim_end  )
def compute_tuning_curve(traces):
    on_period = get_stim_on_traces(traces)
    #on_period = on_period.reshape(on_period.shape[0], on_period.shape[1]*on_period.shape[2])
    try:
        means = on_period.mean(dim='samples')
        means = means.mean(dim='presentations')
    except TypeError as E:
        means = on_period.mean(axis=1)
        means = means.mean(axis=1)
    return means
