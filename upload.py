from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def upload():
    return render_template('file_upload.html')

@app.route('/success1',methods=['POST'])
def success():
    if request.method=='POST':
        f=request.files['file']
        f.save(f.filename)
        return render_template("success1.html",name=f.filename)
if __name__ == '__main__':
    app.run(debug=True)

