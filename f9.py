from flask import Flask,render_template,make_response,request
app=Flask(__name__)
@app.route('/')
def login():
    return render_template('h7.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['pass']
    if password=='Ashish':
        res=make_response(render_template('h8.html'))
        res.set_cookie('email',email)
        return res
    else:
        return render_template("h7.html")

@app.route('/viewprofile')
def viewprofile():
    email=request.cookies.get('email')
    res=make_response(render_template('h9.html',name=email))
    return res

if __name__ == '__main__':
    app.run(debug=True)