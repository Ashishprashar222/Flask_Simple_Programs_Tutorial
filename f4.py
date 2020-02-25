from flask import Flask,render_template
app=Flask(__name__)
@app.route('/a/<int:num>')
def a(num):
    return render_template('h2.html',n=num)
if __name__ == '__main__':
    app.run(debug=True)