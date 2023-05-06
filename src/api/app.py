from flask import Flask
import subprocess
app = Flask(__name__)


  
@app.route('/')
def index():
    return 'Dashboard'
    return 'Use with no args'
    return '{host}/ex2/{command}'
    return 'Use with one arg'
    return '{host}/ex/{command}/{arg}'

   

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
    
  

