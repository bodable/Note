#/bin/bash

date=`date +%Y %m %d`
echo $date
git status
git add .
git add -u
git commit -m "auto commit $date"
git push


#583  git status
#584  git add .
#585  git status
#586  git commit -m "auto commit"
#587  git push

