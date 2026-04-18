@echo off
echo Removing large file from git history...

REM Remove the zst file from the last commit
git rm --cached "Puzzle DB/lichess_db_puzzle.csv.zst"
git rm --cached puzzles_5000.js

REM Add to .gitignore
echo Puzzle DB/ >> .gitignore
echo puzzles_5000.js >> .gitignore
echo apply_fix*.py >> .gitignore
echo extract_puzzles.py >> .gitignore
echo inject_puzzles.py >> .gitignore

REM Amend the last commit to remove the big files
git add .gitignore
git commit --amend --no-edit

REM Force push the fixed commit
git push origin HEAD:main --force

echo Done! Large files removed from git.
