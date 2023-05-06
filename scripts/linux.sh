#!/bin/bash
echo 'Linux Remote-Shell Setup'
echo 'Updating'
sudo apt-get update
echo 'Installing curl'
sudo apt-get install curl
echo 'Downloading script'
curl -o app.py https://raw.githubusercontent.com/shourdev/remote-shell/main/src/api/app.py
echo 'Installing requirements'
sudo apt-get install python3
sudo apt-get install python3-pip python-dev
pip install flask
echo 'Opening file'
echo 'Press ctrl + c to stop and run "python3 app.py" to start again.'
python3 app.py
