if exist venv (
  DEL /F /Q venv\*
  RMDIR /S /Q venv
)
mkdir venv
python -m venv venv
call venv\Scripts\activate.bat
python -m pip install -U pip
python -m pip install -r requirements_win.txt

cscript //B makeshortcut.vbs SkipAdYoutubeEdge %cd% run.bat "edge" %USERPROFILE%\Desktop

reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall" /s | find "Chrome"
if %errorlevel% == 0 (
  makeshortcut.vbs SkipAdYoutubeChrome %cd% run.bat "chrome" %USERPROFILE%\Desktop
)

reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall" /s | find "Firefox"
if %errorlevel% == 0 (
  makeshortcut.vbs SkipAdYoutubefirefox %cd% run.bat "firefox" %USERPROFILE%\Desktop
)

deactivate