from flask import Flask
app=Flask(__name__)
@app.route('/a')
def a():

    return "hello"
if __name__ == '__main__':
    app.run(debug=True)