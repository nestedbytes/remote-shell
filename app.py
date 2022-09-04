from flask import Flask,render_template
import subprocess
app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('index.html')
   

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
    

    


if __name__ == "__main__":
    app.run(debug=False)
