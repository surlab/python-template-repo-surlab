# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py,md
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] colab_type="text" id="view-in-github"
# <a href="https://colab.research.google.com/github/GreggHeller1/replace_with_env_name/blob/main/scripts/notebook.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
# + id="71ee021b"
#settings
# %load_ext autoreload
# %autoreload 2
try:
  import google.colab
  in_colab = True
except:
  in_colab = False
print(in_colab)
# + colab={"base_uri": "https://localhost:8080/"} id="4e02e926" outputId="84475a29-508b-4d96-adf5-e85665e994d2"
#installs (for colab only, run this once)
if in_colab:
    # ! git clone https://github.com/GreggHeller1/replace_with_env_name.git
# + id="5e9731ca"
#local imports
#cwd if in colab for imports to work
if in_colab:
    # %cd /content/replace_with_env_name
    
from src import data_io as io
from src import plotting as plot
from src import computation as comp
from src import helper_functions as hf
import main
# + id="db51ef2e"
#imports
import os

#import xarray as xr
#import pandas as pd
#import numpy as np
#import ipdb
#from matplotlib import pyplot as plt
#from PIL import Image #this needs to be after matplotlib??
#from scipy.stats import stats   
#from neuron import h, gui
# + colab={"base_uri": "https://localhost:8080/"} id="a06b6e4a" outputId="989c69e2-c8c4-43e0-9ba6-7a36f66be4c3"
#define paths
#cwd if in colab for file loading to work
if in_colab:
    # %cd /content/replace_with_env_name/scripts
    
print(os.getcwd())
base_dir = os.path.split(os.getcwd())[0]
test_path = os.path.join(base_dir, 'demo_data', 'test.txt')
print(test_path)
print(os.path.exists(test_path))

data_path = "your data path here"
print(os.path.exists(data_path))

# + colab={"base_uri": "https://localhost:8080/"} id="b3586a50" outputId="56f159c6-3dbc-4b37-d217-083fb5d2e792"
#data inputs
loaded_data = main.main_io()
# + id="82a5927b"
#data manipulation
results = main.main_computation(loaded_data)
# +
#debug speed 
#import cProfile
#cProfile.run('main.main_computation(loaded_data)')
# -

#save results
main.main_saving(results)

#reload results for plotting
loaded_results = main.reload_results_for_plotting()

#make and save plots
main.main_plotting(loaded_results)
