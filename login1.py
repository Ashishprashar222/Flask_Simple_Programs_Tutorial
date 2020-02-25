from flask import Flask,render_template,request,redirect,url_for,abort
app=Flask(__name__)
@app.route('/')
def home1():
    return render_template('home1.html')
@app.route('/llogin1')
def llogin1():
    return render_template("llogin1.html")

@app.route('/valildate',methods=['POST'])
def validate():
    if request.method == 'POST' and request.form['pass'] == 'ashish':
        return redirect(url_for('success2'))
    else:
        abort(401)
@app.route('/success2')
def success2():
    return "login success"
if __name__ == '__main__':
    app.run(debug=True)
