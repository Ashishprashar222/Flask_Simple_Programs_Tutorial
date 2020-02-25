from flask import Flask,render_template

app = Flask(__name__)

@app.route('/message')
def message():
    return render_template('h3.html')

if __name__ == '__main__':
    app.run(debug=True)