REM comment: this script creates a new environment for a repo created from the 
REM comment: template python-template-repo-surlab
REM comment: 1. It creates a conda envirnoment based on the file "environment_cross_platform.yml"
REM comment: 2. It also sets up "src" so they dynamically update when called by files in "scripts"
conda env create -f environment_cross_platform.yml
call conda info --envs
call pip install -e .
