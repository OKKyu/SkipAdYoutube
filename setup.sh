#! /bin/bash

if [ ! -d ./venv ]; then
  mkdir venv
  python3 -m venv venv
fi

source ./venv/bin/activate
pip install -r requirements.txt
deactivate

if [ -d ~/Desktop ] && [ -d ~/.local/share/applications ]; then
  echo "Creating shortcut"
  cp -f ./SkipAdYoutube_firefox.desktop ~/.local/share/applications
  cp -f ./SkipAdYoutube_chrome.desktop ~/.local/share/applications
  
  chromeExist=`whereis google-chrome | wc -w`
  if [ $chromeExist -gt 1 ]; then
     echo "Path="`pwd` >> ~/.local/share/applications/SkipAdYoutube_chrome.desktop
     echo "Exec="`pwd`"/run.sh chrome " >> ~/.local/share/applications/SkipAdYoutube_chrome.desktop
     ln -sf ~/.local/share/applications/SkipAdYoutube_chrome.desktop ~/Desktop/SkipAdYoutube_chrome
  fi
  
  foxExist=`whereis firefox | wc -w`
  if [ $foxExist -gt 1 ]; then
     echo "Path="`pwd` >> ~/.local/share/applications/SkipAdYoutube_firefox.desktop
     echo "Exec="`pwd`"/run.sh firefox " >> ~/.local/share/applications/SkipAdYoutube_firefox.desktop
     ln -sf ~/.local/share/applications/SkipAdYoutube_firefox.desktop ~/Desktop/SkipAdYoutube_firefox
  fi
else
  echo "Desktopディレクトリ、local/share/applicationsが存在しません"
fi
