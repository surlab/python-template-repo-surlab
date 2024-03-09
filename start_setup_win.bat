
REM comment: this script runs some setup procedures to make a repo created from the 
REM comment: template python-template-repo-surlab ready to be used
REM comment: It does the following:
REM comment: 1. searches directory and subdirectories for text files comtaining the string "replace_with_env_name"
REM comment: 	and replaces with the string "env_name" that is entered by the user
REM comment: 2. It then calls install_win.bat to set up the conda environemnt
REM comment: 3. Lastly it calls finish_repo_setup.bat to remove uneeded files


@echo off 
setlocal EnableExtensions DisableDelayedExpansion

set "search=replace_with_env_name"
set /p replace=Please enter the name of the repository (exactly, no spaces):

set "textFile=*.*"
REM comment: Need to replace in .bat, yml, .md, .py and .ipynb files, hopefully this gets all of them and doesn't have any issues...

set "rootDir=."

for /R "%rootDir%" %%j in ("%textFile%") do (
    for /f "delims=" %%i in ('type "%%~j" ^& break ^> "%%~j"') do (
        set "line=%%i"
        setlocal EnableDelayedExpansion
        set "line=!line:%search%=%replace%!"
        >>"%%~j" echo(!line!
        endlocal
    )
)

endlocal

call install_win.bat
call finish_repo_setup.bat