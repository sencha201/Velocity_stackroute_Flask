from flask import Flask
app = Flask(__name__)

@app.route('/')
def testfun():
    return "Welcome to my Flask app"

@app.route('/user/<name>')
def userfun(name):
    return "Welcome %s to flask app" %name

if __name__ == '__main__':
    app.run()