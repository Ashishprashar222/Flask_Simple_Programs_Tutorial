from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')
def hello_name():
   return render_template('hello.html')

if __name__ == '__main__':
   app.run(debug = True)