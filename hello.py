from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import redirect
from flask import abort


app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name

if __name__ == '__main__':
    app.run(debug=True)
    