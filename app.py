from flask import Flask
import subprocess
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to remote shell dashboard!'
   

@app.route('/ex/<string:c>/<string:p>')
def main(c,p):
    result = subprocess.run([c,p], stdout=subprocess.PIPE)
    lines = result.stdout.splitlines()
 
    op = ' '.join([str(elem) for elem in lines])
    return op
    
@app.route('/ex2/<string:c>')
def main2(c):
    result2 = subprocess.run([c], stdout=subprocess.PIPE)
    lines2 = result2.stdout.splitlines()
 
    op2 = ' '.join([str(elem) for elem in lines2])
    return op2
    
@app.route('/console')
def cons():
    


if __name__ == "__main__":
    app.run(debug=False)
