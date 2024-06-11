"""generic description of module config.py(cfg). please update as you develop
config.py should contain parameters that an end user might want to change
whenever possible, variables that are features of the input data should be inferred, not specified
so config should contain only what is user system specific or purely a matter of user preference
examples are whether to save plots, and if so, what to save them as, turning on or off verbose options or specifying a specifigg local path
this can also include functions that are intended to be modified by the end user depending on their data structure
"""


import numpy as np
import os 

################
# main config
#################

cfg.data_path = r"root\your\path\here"



################
# computation config
#################

verbose = False






################
# plotting/saving config
#################

save_plots = True
plot_filetype = 'png' #'svg' or 'png'
