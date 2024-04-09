REM comment: this script runs some setup procedures to make the template scripts 
REM comment: useful for the particular name of the new repo
REM comment: It does the following:
REM comment: 1. searches directory and subdirectories for text files comtaining the string "replace_with_env_name"
REM comment: 	and replaces with the string "env_name" that is entered by the user
REM comment: It is important that this is done FIRST so that create_env creates the right environment name
@echo off 
setlocal EnableExtensions DisableDelayedExpansion
set "search=replace_with_env_name"
set /p replace=Please enter the name of the repository (exactly, no spaces):
set "textFile=*.*"
REM comment: Need to replace in .bat, yml, .md, .py and .ipynb files, hopefully this gets all of them and doesn't have any issues...
set "rootDir=."
for /r %%f in (.\*) do (
    echo "fullname: %%f"
    echo "%%f" |findstr /i ".git">nul || (
    for /f "delims=" %%i in ('type "%%~f" ^& break ^> "%%~f"') do (
        set "line=%%i"
        setlocal EnableDelayedExpansion
        set "line=!line:%search%=%replace%!"
        >>"%%~f" echo(!line!
        endlocal
    )
    )
)
endlocal
