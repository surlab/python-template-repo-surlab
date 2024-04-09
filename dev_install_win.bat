REM comment: this script runs some setup procedures to make a repo created from the 
REM comment: template python-template-repo-surlab ready to be used
REM comment: It does the following:
REM comment: 1. calls replace_repo_name_in_text.bat to substitute the actual repo name in text files
REM comment: 2. It then calls create_env_win.bat to set up the conda environemnt
REM comment: 3. It replaces the readme that contains instructions for using the python-template-repo-surlab
REM comment:    with a reasonable starting readme
REM comment: 4. It deletes all files that are no longer necessary for subsequent use of the repo. 
REM comment: 5 it uses one of the developer scripts to commit and push the changes
REM comment: 6 It attempts to delete itself but seems to fail no matter what I do...

call replace_repo_name_in_text.bat

REM comment: This is here because for some reason this script skips 2 characters after the preceeding call... what a mystery
timeout 5

call "create_env_win.bat"

del ".\README.md"
ren ".\template_readme.md" README.md
del ".\replace_repo_name_in_text.bat"
del ".\create_env_win.bat"
call ".\developer_scripts\simple_WIP_commit_push.bat"

timeout 5

del dev_install_win.bat



