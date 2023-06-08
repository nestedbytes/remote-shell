### Remote-Shell
An free, open source and self hosted api to access a computer's from anywehere <br>
This is an api which can execute commands on your local machine from the web
### Requirements
Python <br>
Flask
### Host instructions
# Linux
```sh
wget https://raw.githubusercontent.com/shourdev/remote-shell/main/scripts/linux.sh
```
```sh
bash linux.sh
```
# Windows
TBA
### USAGE
You can use the api without a client but for ease a client is suggested. <br>
I currently have made the client for cli and other client for platforms like phone and web will be out soon <br>
[Official CLI Client](https://github.com/shourdev/rs-cli) <br>
For the api needed in these clients its basicly your host url like `www.myserver.com/ex/` so your api on the /ex/ route is your api which will be needed to use these clients. Ex: 
```sh
www.myvps.com/ex/
```
