from flask import Flask,render_template_string
import subprocess
app = Flask(__name__)

passw = "" # set your password here
  
@app.route('/')
def index():
    return render_template_string('''<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="css url"/>
    </head>
    <body>
       <h1> Dashboard </h1>
        <p>Run command</p> <br>
        <p> {host}/ex/{password}/{command}/{arg}/ </p> <br>
         <p> API: </p> <br>
 <p> {host}/ex/ </p>      
    </body>
</html>
'''

   )

@app.route('/ex/<string:password>/<path:args>')
def main(password,args):
    if password == passw:
        
        cmd = args.split('/')
        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        lines = result.stdout.splitlines()
        op = ' '.join([elem.decode() for elem in lines])
        return op
    else:
        return "wrong password"



if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
