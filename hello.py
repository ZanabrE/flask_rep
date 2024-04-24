from flask import Flask, render_template, session, url_for, flash
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET KEY'] = 'hard to guess string'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        name = request.form['name']
        session["name"] = name
        flash("Login Successful!")
        return redirect(url_for('user'))
    else:
        if "name" in session:
            return redirect(url_for('user'))
        return render_template('login.html')

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('user'))
    else:
        return render_template('register.html')

@app.route('/workout_1', methods=["POST", "GET"])
def workout_1():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('user'))
    else:
        return render_template('workout_1.html')

@app.route('/workout_2', methods=["POST", "GET"])
def workout_2():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('user'))
    else:
        return render_template('workout_2.html')

@app.route('/workout_3')
def workout_3():
    return render_template('workout_3.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name

#@app.errorhandler(404)
#def page_not_found(e):
    #return render_template('404.html'), 404

#@app.errorhandler(500)
#def internal_server_error(e):
    #return render_template('500.html'), 500
    
if __name__ == '__main__':
    app.run(debug=True)
    