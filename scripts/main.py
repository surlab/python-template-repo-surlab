"""generic description of this module, main.py(main). please update as you develop
main.py organizes the functions from the src modules into a useable order allowing end to end operation 
with a single function call 
Sometimes this includes looping through multiple datasets, aggregating data, etc
Each of these main_xyz functions should correspond to a block in your demo jupyter notebook 
with additional explanation
"""
from src import config as cfg
from src import plotting as plot
from src import computation as comp
from src import helper_functions as hf

import os

def main():
    loaded_data = main_io()
    results = main_computation(loaded_data)
    main_saving(results)
    loaded_results = reload_results_for_plotting()
    main_plotting(loaded_results)


def main_loading():
    #functions from data_io
    path = cfg.data_path
    loaded_data = io.load_data(path)
    return loaded_data

def main_computation(loaded_data):
    #functions from computation
    intermediat_results = comp.run_analysis_1(loaded_data)
    results = comp.run_analysis_2(intermediat_results)
    return results
    
def main_saving(results):
    #functions from data_io
    io.save_results(path)

def reload_results_for_plotting():
    #functions from data_io
    loaded_results = io.load_results(path)
    return loaded_results

def main_plotting(loaded_results):
    #functions from plotting
    plot.plot_results(loaded_results)


if __name__ == "__main__":
    main()
