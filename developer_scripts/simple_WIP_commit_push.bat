REM comment: This script commits all changes and pushes with a default WIP (work in progress) message
call git add --all
call git commit -m "WIP: unstable code committed and pushed by shortcut script"
call git push
