from math import sin,cos,tan,pow
from flask import Flask, render_template, request
app = Flask(__name__)
def evaluate(a):
    return eval(a)

@app.route('/', methods=['GET', 'POST'])
def index():
    cal="="
    res=0
    if request.method == 'POST':
        cal=request.form['cal']
        if(cal=="="):
            exp=request.form['exp']
            res=evaluate(exp)
            print(cal,res,exp)
    return render_template("index.html",res=res,cal=cal)

if __name__ == '__main__':
    app.run()