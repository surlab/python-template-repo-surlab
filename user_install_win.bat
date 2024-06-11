REM comment: this script runs some setup procedures to make a repo created from the 
REM comment: template python-template-repo-surlab ready to be used
REM comment: It does the following:
REM comment: 1. calls replace_repo_name_in_text.bat to substitute the actual repo name in text files
REM comment: 2. It then calls create_env_win.bat to set up the conda environemnt
REM comment: 3. It calls finish_repo_setup.bat to remove uneeded files, and pushes the changes
call ".\developer_scripts\create_env_win.bat"
echo "Finished with install!!"
( del /q /f "%~f0" >nul 2>&1 & exit /b 0  )
@ECHO OFF
SETLOCAL
del user_install_win.bat
DEL "%~f0"
(goto) 2>nul & del "%~f0"
cmd /k
( del /q /f "%~f0" >nul 2>&1 & exit /b 0  )
