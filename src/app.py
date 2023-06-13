from flask import Flask,render_template_string
import subprocess
app = Flask(__name__)

passw = "" # set your password here
  
print("Your api is (hosturl)/ ")

@app.route('/<string:password>/<path:args>')
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
