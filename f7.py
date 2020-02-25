from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def abc():
    return render_template('h5.html')

@app.route('/success',methods = ['POST', 'GET'])
def print_data():
   if request.method == 'POST':
      result = request.form
      return render_template("h6.html",result = result)
if __name__ == '__main__':
    app.run(debug=True)
