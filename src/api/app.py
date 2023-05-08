from flask import Flask,render_template_string
import subprocess
app = Flask(__name__)


  
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
        <p> {host}/ex/{command}/{arg} </p>
      
    </body>
</html>
'''

   )

@app.route('/ex/<path:args>')
def main(args):
    cmd = args.split('/')
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    lines = result.stdout.splitlines()
    op = ' '.join([elem.decode() for elem in lines])
    return op



if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
