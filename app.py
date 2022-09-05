from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import subprocess
app = Flask(__name__)
app.config['SECRET_KEY'] = 'NOBODY-CAN-GUESS-THIS'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()
class DataBase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(20))
  
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
    
@app.route('/setpas/<string:ps>')
def pas(ps):
    newpas = DataBase(password=ps)
    db.session.add(newpas)
    db.session.commit()



if __name__ == "__main__":
    app.run(debug=False)
    db.create_all()