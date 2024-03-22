REM comment: this script runs some setup procedures to make a repo created from the 
REM comment: template python-template-repo-surlab ready to be used
REM comment: It does the following:
REM comment: 1. calls replace_repo_name_in_text.bat to substitute the actual repo name in text files
REM comment: 2. It then calls create_env_win.bat to set up the conda environemnt
REM comment: 3. Lastly it calls finish_repo_setup.bat to remove uneeded files
call replace_repo_name_in_text.bat
call install_win.bat
call finish_repo_setup.bat
