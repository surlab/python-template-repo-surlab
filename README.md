# python-template-repo-surlab
Template repository for convenient setup of new python repos
Following these instructions will create a new repo with appropriate directory structure and files, create an appropriate conda environment, and hopefully ensure that the bat scripts work for automating common operations for users that prefer not to use the command line (updating the environment files, creating and pushing work in progress (WIP) commits, opening a prompt and activating the environemnt, opening jupyter notebook/lab, and running scripts/main.py)
####Instructions
1. Update the python version if necessary. Currently, following these instructions will set up a conda environment using python 3.8 If this is out of date, the environment_cross_platform.yml in THIS template repo should be updated (both remote and local) to reflect the current version before proceeding. (Please also update this step in this readme as well.)
1. Make sure conda is in your windows path (you can check this by opening a new command prompt (search CMD) and entering the following command

        >>>conda info --envs

    If this works, you are good to go. Otherwise you need to install anaconda or add it to your windows path. See answer here by "Simba" https://stackoverflow.com/questions/44597662/conda-command-is-not-recognized-on-windows-10
1. Follow the instructions here to create a repository from this template: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
1. Clone the newly created repository to a windows (10?) machine
1. Double click the file "dev_install_win" or "dev_install_win.bat" to run it. This will ask for text string nae of the newly created repository, and will use this to replace any instance of "replace_with_env_name" found in the contained text documents. 
1. Thats it!
