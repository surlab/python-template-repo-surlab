import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns
from src import config as cfg
from src import computation as comp
from src import helper_functions as hf
## how should this work?
#Start with the raw traces.
#Subsample. Is this a stop point or should each sorting aply the sampling?
#Generate the sort mat - needs to be able to be applied to another easily
#right now for columns and rows this isn't actually a matrix... we just pass in the matrix to sort by.
#sort by this matrix - produces mat.
#^^^Sometimes we have this leaving in 2d, sometimes we have brought to 2d already... which one?
#the only reason to leave it 2d is if we want to apply a preferred idrection sorting after
#which most of the time we may want to do because this is something that parses the response nicely.
# the big thing that we want to do is sort across directions by the soma response.
#AND ALSO within directions by the spine response (amplitude, peak time, whatever. )
#I think we want to apply the Across sorting second, since the within shuffles will mess it up.
#so we want to produce a matrix from the within sorts
##########################################################################
#For the main_plotting_loop... should just put that here too??
def plot_model_simulation_scores(df, prefix=''):
    fig, ax = plt.subplots()
    sns.lineplot(data=df.loc[df['responsive_status'] == 'unresponsive'], x='model_type', y='model_soma_similarity_score', hue='experiment_id',
                 palette='Blues', marker='o')
    sns.lineplot(data=df.loc[df['responsive_status'] == 'responsive'], x='model_type', y='model_soma_similarity_score', hue='experiment_id',
                 palette='Reds', marker='o')
    plt.xticks(rotation=45)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ## Get the legend handles and add them to plt.legend, so that the right handles are addigned
    #legend_handles, _= plt.gca().get_legend_handles_labels()
    #plt.legend(handles = legend_handles, loc='right',
    #           labels=['Group 1: C1', 'Group 1: C2', 'Group 2: C1', 'Group 2: C2'])
    figname = f'{prefix}{"-"*bool(prefix)}model_performance_summaries.png'
    fig_path = os.path.join(cfg.collect_summary_at_path, figname)
    print(f'Saving figure to {fig_path}')
    fig.savefig(fig_path, bbox_inches='tight')
def plot_model_simulation_scores_bar(df, prefix=''):
    fig, ax = plt.subplots()
    #sns.lineplot(data=df.loc[df['responsive_status'] == 'unresponsive'], x='model_type', y='model_soma_similarity_score', hue='experiment_id',
    #             palette='Blues', marker='o')
    #sns.lineplot(data=df.loc[df['responsive_status'] == 'responsive'], x='model_type', y='model_soma_similarity_score', hue='experiment_id',
    #             palette='Reds', marker='o')
    sns.barplot(data=df.loc[df['responsive_status'] == 'responsive'], x='model_type', y='model_soma_similarity_score', color = 'r', alpha=.3)
    sns.barplot(data=df.loc[df['responsive_status'] == 'unresponsive'], x='model_type', y='model_soma_similarity_score', color = 'b', alpha=.3)
    plt.xticks(rotation=45)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ## Get the legend handles and add them to plt.legend, so that the right handles are addigned
    #legend_handles, _= plt.gca().get_legend_handles_labels()
    #plt.legend(handles = legend_handles, loc='right',
    #           labels=['Group 1: C1', 'Group 1: C2', 'Group 2: C1', 'Group 2: C2'])
    figname = f'{prefix}{"-"*bool(prefix)}model_performance_summaries_bar.png'
    fig_path = os.path.join(cfg.collect_summary_at_path, figname)
    print(f'Saving figure to {fig_path}')
    fig.savefig(fig_path, bbox_inches='tight')
def plot_all_simulation_scores(df):
    #Just use seaborn you idiot? ugh but the normalization hasn't been done.
    #plot_model_simulation_scores(df)
    plot_model_simulation_scores(df, prefix='')
    #So we just have to do this part manually
    exp_ids = df['experiment_id'].unique()
    for exp_id in exp_ids:
        bool_index = df['experiment_id'] == exp_id
        exp_df = df[bool_index]
        democratic_index = exp_df['model_type'] == 'democratic'
        print(democratic_index)
        print('%%%%%%')
        democratic_sim_score = float(exp_df[democratic_index]['model_soma_similarity_score'])
        print(democratic_sim_score)
        exp_df['model_soma_similarity_score'] = exp_df['model_soma_similarity_score']/democratic_sim_score
        print(exp_df['model_soma_similarity_score'])
        #put it back in the larger data frame
        df[bool_index] = exp_df
    plot_model_simulation_scores(df, prefix='normalized')
    plot_model_simulation_scores_bar(df, prefix='normalized')
def plot_simulation_tuning_curves(df, prefix=''):
        ############
        #Plots and output - loop through the CSV and produce this
        ############
        #unpack the df
        df_dict = {}
        print(df.head())
        for index, row in df.iterrows():
            df_dict[index] = row
            print(row)
        #Tuning curve plots
        ############
        fig, axs = plt.subplots(nrows=4, ncols=1)
        linear_model_sub_dict = {k: df_dict[k] for k in ('soma','democratic', 'spine_size', 'distance_to_soma')}
        _, ax = plot_tuning_curves(axs[0], **linear_model_sub_dict)
        responsive_model_sub_dict = {k: df_dict[k] for k in ('soma','democratic', 'unresponsive', 'responsive')}
        _, ax = plot_tuning_curves(axs[1], **responsive_model_sub_dict)
        size_sub_dict = {k: df_dict[k] for k in ('soma','top_20_size', 'bottom_20_size', 'random_20')}
        _, ax = plot_tuning_curves(axs[2], **size_sub_dict)
        dist_sub_dict = {k: df_dict[k] for k in ('soma','top_20_distance', 'bottom_20_distance', 'random_20')}
        _, ax = plot_tuning_curves(axs[3], **dist_sub_dict)
        #Save the Plot
        figname = f"{prefix}{'_'*bool(prefix)}model_tuning_curves.png"
        fig_path = os.path.join(cfg.collect_summary_at_path, figname)
        print(f'Saving figure to {fig_path}')
        fig.savefig(fig_path, bbox_inches='tight')
        #Response timing plot
        ###########
