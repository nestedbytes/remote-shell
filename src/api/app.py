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
        <p>One argument</p> <br>
        <p> {host}/ex/{command}/{arg} </p>
       <p> No arguments </p>  <br>
      <p> {host}/ex2/{command} </p>
    </body>
</html>
'''

   )

@app.route('/ex/<string:c>/<string:p>')
def main(c,p):
    result = subprocess.run([c,p], stdout=subprocess.PIPE)
    lines = result.stdout.splitlines()
 
    op = ' '.join([elem.decode() for elem in lines])

    return op
    
@app.route('/ex2/<string:c>')
def main2(c):
    result2 = subprocess.run([c], stdout=subprocess.PIPE)
    lines2 = result2.stdout.splitlines()
    op2 = ' '.join([elem.decode() for elem in lines2])
    return op2
    


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
