REM comment: this script runs some setup procedures to make a repo created from the 
REM comment: template python-template-repo-surlab ready to be used
REM comment: It does the following:
REM comment: 1. It replaces the readme that contains instructions for using the python-template-repo-surlab
REM comment:    with a reasonable starting readme
REM comment: 2. It deletes all files that are no longer necessary for subsequent use of the repo (including this one). 

del ".\README.md"
ren ".\template_readme.md" README.md

del ".\replace_repo_name_in_text.bat"
del ".\install_win.bat"
del ".\finish_repo_setup.bat"
del ".\create_env_win.bat"