# replace_with_env_name
Description of repository here
## Installation instructions
These instructions require:
1. a recent Python distribution, preferably anaconda 
1. an installation of git. 
1. (@devs don't forget to indicate if visual studio or other software is required)
1. The correct environment yamls. Please check the two environment files before trusting them - The dev should do make sure these work before deployment but may have gotten lazy. Packages only available through pip are not automatically included in the environment_cross_platform.yml. If there are dependancies under pip in the environment_explicit.yml file, consider copying them to the environment_cross_platform.yml or be prepared to pip install them yourself.
#### For a windows machine:
1. Open a command prompt and run the following commands
```bash
cd ..\documents\code #or similar as relevant for your machine
git clone git@github.com:surlab/replace_with_env_name.git
```
2. Double click the file "user_install_win.bat" to run it. This should set up the conda environment and all dependencies. 
#### OR For a windows or non -indows machine
Open a teriman and run the following commands
```bash
cd ..\documents\code #or similar as relevant for your machine
git clone git@github.com:surlab/replace_with_env_name.git
cd replace_with_env_name
conda env create -f environment_cross_platform.yml
Conda activate replace_with_env_name
call pip install -e .
```
The installation should now be complete and the replace_with_env_name conda environment should still be activated. 
## Usage instructions
1. make a copy of default_config.py and name it config.py.
1. change the path in config.py to a data directory containing the appropriate input files defined below
#### For a windows machine:
Double click the file "main.bat" to run it. 
#### OR For a windows or non -indows machine
Open a terminal and run the following commands
```bash
cd path/to/replace_with_env_name
conda activate replace_with_env_name
python scripts/main.py
```
### Input Files:
The code expects to find a directory or tree of nested directories where some the following files in each directory:
1. input file 1 description
1. input file 2 description
### Output Files:
Running the code sucessfully produces the following files
1. input file 1 description
1. input file 2 description
# Quality Control (QC)
It is important that you QC the results of this code and do not trust it blindly. Here is my process for QC.
1. Some of the output files should be images. look through them for the following htings:
# Credit
This code was created for the surlab at MIT by _________. 
The template for this repository was created by Gregg Heller.  
