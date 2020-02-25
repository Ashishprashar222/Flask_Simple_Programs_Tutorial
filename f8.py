from flask import Flask,make_response
app=Flask(__name__)
@app.route('/cookie')
def cookie():
    res=make_response("cookie is set")
    res.set_cookie('good','day')
    return res
if __name__ == '__main__':
    app.run(debug=True)