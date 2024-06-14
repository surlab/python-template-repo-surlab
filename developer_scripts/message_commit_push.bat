REM comment: This script commits all changes and pushes with a default WIP (work in progress) message
call git status

set /p message=Please enter your commit message:
call git add --all
call git commit -m "%message%"
call git push
cmd /k
