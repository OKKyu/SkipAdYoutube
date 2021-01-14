@echo off
call venv\Scripts\activate.bat
python SkipAdYoutube.py 1 %1
deactivate
exit