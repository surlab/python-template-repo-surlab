from src import plotting as plot
from src import config as cfg
import os
import pandas as pd
def main_plotting_loop():
    for filename in os.listdir(cfg.collect_summary_at_path):
        if 'simulation_mean_stim_response' in filename:
            pass
            #exp = filename.split('_')[0]
            #print(f'creating plots for {exp}')
            #fullpath = os.path.join(cfg.collect_summary_at_path, filename)
            #df = pd.read_csv(fullpath, index_col='model_keyword (V), stimulus (->)')
            #df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            #print(df.columns)
            #plot.plot_simulation_tuning_curves(df, prefix=exp)
        if 'single_neuron_simulation_scores' in filename:
            pass
            fullpath = os.path.join(cfg.collect_summary_at_path, filename)
            df = pd.read_csv(fullpath, index_col=0)
            plot.plot_all_simulation_scores(df)
if __name__ == "__main__":
    main_plotting_loop()
