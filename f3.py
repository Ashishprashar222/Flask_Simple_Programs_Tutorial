from flask import Flask,render_template
app=Flask(__name__)
@app.route('/hii/<name>')
def hii(name):
    return render_template('h1.html',name=name)
if __name__ == '__main__':
    app.run(debug=True)