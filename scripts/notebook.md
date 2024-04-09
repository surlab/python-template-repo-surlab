---
jupyter:
  jupytext:
    formats: ipynb,py,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.4
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---
<!-- #region colab_type="text" id="view-in-github" -->
<a href="https://colab.research.google.com/github/GreggHeller1/replace_with_env_name/blob/main/scripts/notebook.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
<!-- #endregion -->
```python id="71ee021b"
#settings
%load_ext autoreload
%autoreload 2
try:
  import google.colab
  in_colab = True
except:
  in_colab = False
print(in_colab)
```
```python colab={"base_uri": "https://localhost:8080/"} id="4e02e926" outputId="84475a29-508b-4d96-adf5-e85665e994d2"
#installs (for colab only, run this once)
if in_colab:
    ! git clone https://github.com/GreggHeller1/replace_with_env_name.git
```
```python id="5e9731ca"
#local imports
#cwd if in colab for imports to work
if in_colab:
    %cd /content/replace_with_env_name
    
from src import data_io as io
from src import plotting as plot
from src import computation as comp
from src import helper_functions as hf
```
```python id="db51ef2e"
#imports
import xarray as xr
#import pandas as pd
import numpy as np
import ipdb
from matplotlib import pyplot as plt
from PIL import Image #this needs to be after matplotlib??
from scipy.stats import stats   
import os
#from neuron import h, gui
```
```python
```
```python
```
```python colab={"base_uri": "https://localhost:8080/"} id="a06b6e4a" outputId="989c69e2-c8c4-43e0-9ba6-7a36f66be4c3"
#define paths
#cwd if in colab for file loading to work
if in_colab:
    %cd /content/replace_with_env_name/scripts
    
test_path = os.path.join('demo_data', 'test.txt')
print(test_path)
print(os.getcwd())
print(os.path.exists(test_path))
soma_path = "/Users/Gregg/code/replace_with_env_name/scripts/demo_data/ASC26_cell_3_soma.mat"
spines_path = "/Users/Gregg/code/replace_with_env_name/scripts/demo_data/ASC26_cell_3_spines.mat"
spines_path = "/Users/Gregg/Dropbox (MIT)/2021 Gregg Sur rotation/ASC_experimental_data/2022-11 Soma Data/ASC15.mat"
print(os.path.exists(soma_path))
print(os.path.exists(spines_path))
```
```python colab={"base_uri": "https://localhost:8080/"} id="b3586a50" outputId="56f159c6-3dbc-4b37-d217-083fb5d2e792"
#data inputs
#io.readfile(test_path)
soma = io.loadmat(soma_path)
spine_data = io.loadmat(spines_path)
soma_data = soma
```
```python id="82a5927b"
#data manipulation
spines = spine_data
type(spines)
print(spines[0].shape)
print(soma[3])
print(spines['dend_cell'])
#print(np.shape(soma['soma_cell']))
#print(np.shape(spines['dend_cell']))
#print(soma['soma_cell'][0,3]._fieldnames)
```
```python
#print(spines.keys())
#print(np.shape(soma[3]))
#print(soma[3].keys())
soma_field_2 = io._todict(soma[2])
spine_field_2 = io._todict(soma[2])
#ref = spine_field_2['dend_cell'][2,0]
#spine_field_2 = spines[ref]#['DSI']
#print(np.array(field_2))
#print(field_2['vis_stim_times'])
#spines_f2 = 
```
```python
print(spine_field_2['trial_traces'].shape)
```
```python
soma_traces = np.array(soma_field_2['trial_traces'])
spine_traces = np.array(spine_field_2['trial_traces'][:,:,0,:,0].swapaxes(0,-1))
fovs = spine_data['dend_cell'][2,:].shape[0]
print(fovs)
print(soma_traces.shape)
print(spine_traces.shape)
#trial_amps = np.array(field_2['trial_amp'])
#print(trial_amps.shape)
```
```python
soma_traces = hf.get_traces(soma_data)
spine_traces = hf.get_traces(spine_data)
```
```python
metadata = hf.get_spine_metadata(spine_data, fov_num = 0)
print(len(hf.get_neck_length(spine_data)['stem_stats']))
```
```python
soma_sub_traces = comp.select_timesteps(soma_traces)
```
```python
plot.plot_activity_plots(soma_sub_traces)
```
```python
plt.plot(hf.get_precomputed_tuning_curve(soma_data))
```
```python
summed_spine_traces_1 = comp.get_summed_trial_sampled_spine_trace(spine_data)
sum_spine_sub_traces = comp.select_timesteps(summed_spine_traces_1)
```
```python
plot.plot_activity_plots(sum_spine_sub_traces)
```
```python
import cProfile
cProfile.run('summed_spine_traces = comp.get_summed_trial_sampled_spine_trace(spine_data)')
#summed_spine_traces = comp.get_summed_trial_sampled_spine_trace(spine_data)
sum_spine_sub_traces = comp.select_timesteps(summed_spine_traces)
```
```python
plot.plot_activity_plots(sum_spine_sub_traces)
```
```python
means = comp.compute_tuning_curve(soma_traces)
print(means.shape)
soma_means = means/max(means)
plt.plot(soma_means, label='measured soma response')
means = comp.compute_tuning_curve(summed_spine_traces_1)
means = means/max(means)
plt.plot(means, label='sum spines')
means = comp.compute_tuning_curve(summed_spine_traces)
sampled_means = means/max(means)
plt.plot(sampled_means, label='sum sampled spines')
plt.plot(hf.get_precomputed_tuning_curve(soma_data), label='kyles')
plt.legend()
print(f'{stats.pearsonr(soma_means, sampled_means)}')
```
```python
all_spine_activity_array, spines_per_fov_list = comp.compile_spine_traces(spine_data)
model_output = comp.compute_model_output_from_random_sampled_fovs(spine_data, all_spine_activity_array, spines_per_fov_list, simulated_trials_per_stim=100)
means = comp.compute_tuning_curve(model_output)
means = means/max(means)
plt.plot(means, label='democratic spines simulated response')
plt.plot(soma_means, label='measured soma response')
kyle_means = hf.get_precomputed_tuning_curve(soma_data)
#mean_amp should be mean of all the trials
#excluded trials where the baseline was elevated
#trial amps is mean of stim on - mean o baseline, then average
#stim on is 41-50 (0-.9)
#baseline is 21-40 (-2:-.1)
#also median and von mieses
kyle_means = kyle_means/max(kyle_means)
plt.plot(kyle_means, label = 'kyle_computed')
plt.legend()
```
```python
#plot.plot_activity_plots(np.array(model_output))
plt.imshow(plot.flatten_for_image(np.array(model_output)), aspect='auto')
```
```python
plt.imshow(plot.flatten_for_image(soma_traces), aspect='auto')
```
```python
weighted_traces = comp.weights_size_lin(spine_data, all_spine_activity_array)
weighted_traces.shape
spine = 1
stim = 6
pres = 0
plt.plot(weighted_traces[spine,stim,pres,:])
plt.plot(all_spine_activity_array[spine,stim,pres,:])
```
```python
all_spine_activity_array, spines_per_fov_list = comp.compile_spine_traces(spine_data, subset='unresponsive')
unresponsive_model_output = comp.compute_model_output_from_random_sampled_fovs(spine_data,
    all_spine_activity_array, spines_per_fov_list, simulated_trials_per_stim=100,
)
unresponsive_means = comp.compute_tuning_curve(unresponsive_model_output)
unresponsive_means = unresponsive_means/max(unresponsive_means)
all_spine_activity_array, spines_per_fov_list = comp.compile_spine_traces(spine_data, subset='responsive')
responsive_model_output = comp.compute_model_output_from_random_sampled_fovs(spine_data,
    all_spine_activity_array, spines_per_fov_list, simulated_trials_per_stim=100,
)
responsive_means = comp.compute_tuning_curve(responsive_model_output)
responsive_means = responsive_means/max(responsive_means)
```
```python
plt.plot(unresponsive_means, label='unresponsive democratic')
plt.plot(responsive_means, label='responsive democratic')
plt.plot(means, label='all democratic spines simulated response')
plt.plot(soma_means, label='measured soma response')
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
```
```python
selected_timesteps = comp.select_timesteps(np.array(unresponsive_model_output))
new_idx = plot.sort_by_onset_time(selected_timesteps)#, plot.sort_by_mean_amp)
ordered_traces = plot.use_as_index(new_idx, selected_timesteps)
#plt.imshow(ordered_traces, aspect='auto')
plt.imshow(plot.flatten_for_image(selected_timesteps), aspect='auto')
```
```python
selected_timesteps = comp.select_timesteps(np.array(responsive_model_output))
new_idx = plot.sort_by_onset_time(selected_timesteps)#, plot.sort_by_mean_amp)
ordered_traces = plot.use_as_index(new_idx, selected_timesteps)
#plt.imshow(ordered_traces, aspect='auto')
plt.imshow(plot.flatten_for_image(selected_timesteps), aspect='auto')
```
```python
all_spine_activity_array, spines_per_fov_list = comp.compile_spine_traces(spine_data)
size_model_output = comp.compute_model_output_from_random_sampled_fovs(spine_data,
    all_spine_activity_array, spines_per_fov_list, simulated_trials_per_stim=100,
    weight_function = comp.weights_size_lin
)
size_means = comp.compute_tuning_curve(size_model_output)
size_means = size_means/max(size_means)
dist_model_output = comp.compute_model_output_from_random_sampled_fovs(spine_data,
    all_spine_activity_array, spines_per_fov_list, simulated_trials_per_stim=100,
    weight_function = comp.weights_distance_lin
)
dist_means = comp.compute_tuning_curve(dist_model_output)
dist_means = dist_means/max(dist_means)
```
```python
    
plt.plot(size_means, label='weighted by size spines')
plt.plot(dist_means, label='weighted by distance from soma')
plt.plot(democratic_means, label='democratic spines simulated response')
plt.plot(soma_means, label='measured soma response')
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
```
```python
selected_timesteps = comp.select_timesteps(np.array(size_model_output))
new_idx = plot.sort_by_onset_time(selected_timesteps)#, plot.sort_by_mean_amp)
ordered_traces = plot.use_as_index(new_idx, selected_timesteps)
plt.imshow(ordered_traces, aspect='auto')
#plt.imshow(plot.flatten_for_image(selected_timesteps), aspect='auto')
```
```python
selected_timesteps = comp.select_timesteps(np.array(dist_model_output))
new_idx = plot.sort_by_onset_time(selected_timesteps)#, plot.sort_by_mean_amp)
ordered_traces = plot.use_as_index(new_idx, selected_timesteps)
plt.imshow(ordered_traces, aspect='auto')
#plt.imshow(plot.flatten_for_image(selected_timesteps), aspect='auto')
```
```python
selected_timesteps = comp.select_timesteps(soma_traces)
new_idx = plot.sort_by_onset_time(selected_timesteps)#, plot.sort_by_mean_amp)
ordered_traces = plot.use_as_index(new_idx, selected_timesteps)
plt.imshow(ordered_traces, aspect='auto')
#plt.imshow(plot.flatten_for_image(selected_timesteps), aspect='auto')
```
```python
a = np.zeros((136, 16, 10, 91))
print(a.shape)
b = np.arange(0, a.shape[0], 1)
print(len(b))
c = np.random.randint(0,9, len(b))
print(c)
#lets try to grab the 1st presentation for spine 1 and the second for spine 2
sliced = a[b, :, c, :]
print(sliced.shape)
```
```python
a = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12]])
print(a.shape)
a[(1,0,1,0,1,0), (0,1,2,3,4,5)]
```
```python
spine_sub_traces = comp.select_timesteps(spine_traces)
print(spine_traces.shape)
print(spine_sub_traces.shape)
```
```python
plot.plot_activity_plots(spine_sub_traces)
```
```python
plot.plot_activity_plots(soma_sub_traces)
```
```python
all_spine_activity_array, spines_per_fov_list = comp.compile_spine_traces(spine_data, subset='all')
zeta_list = []
for i, (fov_activity_meta, fov_metadata )in enumerate(hf.fov_generator(spine_data)):
    zeta_list.extend(list(hf.get_fov_zetas(fov_activity_meta)))
similarity_list, spine_num_list = plot.get_most_similar_spine(soma_data, all_spine_activity_array)
#spine_means, spine_means_sorted, spine_bool = plot.produce_activity_plots(best_match_traces)  
responsive_idxs = list(np.where(np.array(zeta_list) <=.05)[0])
responsive_ranks = []
for i, spine_idx in enumerate(spine_num_list):
    if spine_idx in responsive_idxs:
        responsive_ranks.append(i)
print(responsive_ranks)
unresponsive_idxs = list(np.where(np.array(zeta_list) >.05)[0])
unresponsive_ranks = []
for i, spine_idx in enumerate(spine_num_list):
    if spine_idx in unresponsive_idxs:
        unresponsive_ranks.append(i)
print(unresponsive_ranks)
```
```python
#for rank in range(10):
for rank in unresponsive_ranks[:10]:
#for rank in responsive_ranks[:10]:
    #best_match_traces = comp.get_traces(spine_data, fov=fov_num_list[rank], spine_index=spine_num_list[rank])
    best_match_traces = comp.select_timesteps(all_spine_activity_array[spine_num_list[rank],:,:,:])
    global_spine_num = spine_num_list[rank]
    (fov_i, spine_fov_i) = hf.get_fov_idx_from_all_spine_idx(global_spine_num, spine_data)
    print(f'global spine_num: {global_spine_num}, this is the {spine_fov_i}th spine in fov {fov_i}')
    plot.plot_activity_plots(np.array(best_match_traces))
```
```python
```
```python
stim_repeats = 10
np.random.randint(0,stim_repeats, (3,4,5))
```
```python
fov = 0
type(fov) is int
```
```python
a = np.array([0,0,2,0,0,0,1,0,0,0,0,0,0,3,0,0])
```
```python
```
```python
np.roll(a, -(np.argmax(a)-7))
```
```python
-4%16
```
```python
import matplotlib.colors as cm
```
```python
num_cells = 20
responsive_colors = [ plt.get_cmap('autumn')(x) for x in np.linspace(0, 1, num_cells)]
unresponsive_colors = [ plt.get_cmap('winter')(x) for x in np.linspace(0, 1, num_cells)]
#From here https://stackoverflow.com/questions/8931268/using-colormaps-to-set-color-of-line-in-matplotlib 
```
```python
responsive_count = 0
unresponsive_count = 0
for i in range(num_cells):
    data = np.random.random(16)
    if i%2:
        color_val = responsive_colors[responsive_count]
        responsive_count+=1
    else:
        color_val = unresponsive_colors[unresponsive_count]
        unresponsive_count+=1
    plt.plot(data, color=color_val)
```
```python
soma_field_2 = io._todict(soma_data[2])
tuning_curve = hf.get_precomputed_tuning_curve(soma_data)
preferred_stim_index = np.argmax(tuning_curve)
zeta_results = soma_field_2['ZETA_test_dir'][preferred_stim_index]
p_value = io._todict(zeta_results)['dblP']
```
```python
print(p_value)
```
```python
from scipy import stats
from PIL import Image
import imageio
```
```python
stats.pearsonr([1,2,3], [4,5,6])
```
```python
test_array = np.random.randint(0,200,(16,16))
test_array = np.random.rand(16,16)#*30
data = test_array
path = 'demo_data/my_image.tiff'
img1 = Image.fromarray(data)
img1.save(path)
test_read = np.array(Image.open(path))
#f1 = list(img1.getdata())
#f2 = list(img2.getdata())
#print(f1 == f2)
#print(f1)
#test_array = np.tile(test_array,(3,1,1))
#test_array = np.moveaxis(test_array,0, 2)
#print(test_array.shape)
#im_pil = Image.fromarray(test_array)
##from here https://stackoverflow.com/questions/71272571/cant-recover-the-same-numpy-array-from-pil-saved-png-image
#path = 'demo_data/my_image.Tiff'
#im_pil.save(f, 'TIFF')
#plt.imsave(path, test_array, cmap=plt.cm.gray)
```
```python
with Image.open(path) as im:
        test_read = np.array(im)
test_read.shape
```
```python
test_read[0,:]
```
```python
test_array[0,:]
```
```python
import pandas as pd
import seaborn as sns
```
```python
fullpath = "/Users/Gregg/Dropbox (MIT)/2021 Gregg Sur rotation/ASC_experimental_data/adult_spine_model_results/single_neuron_simulation_scores.csv"
df = pd.read_csv(fullpath, index_col=0)
df.head()
```
```python
data = {'group': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],
        'block': [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3],
        'cond': ['c1', 'c2', 'c1', 'c2', 'c1', 'c2', 'c1', 'c2', 'c1', 'c2', 'c1', 'c2'],
        'value': [1, 2, 1.2, 2.1, 1.1, 2.2, 3, 4, 3.3, 4.1, 3.1, 4]}
df_2=pd.DataFrame(data)
df_2.head()
```
```python
sns.lineplot(data=df.loc[df['unrespons'] == 1], x='block', y='value', hue='cond',
             palette='Blues', marker='o')
sns.lineplot(data=df.loc[df['group'] == 2], x='block', y='value', hue='cond',
             palette='Reds', marker='o')
## Get the legend handles and add them to plt.legend, so that the right handles are addigned
legend_handles, _= plt.gca().get_legend_handles_labels()
plt.legend(handles = legend_handles, title='Legend', loc='right',
           labels=['Group 1: C1', 'Group 1: C2', 'Group 2: C1', 'Group 2: C2'])
plt.show()
```
