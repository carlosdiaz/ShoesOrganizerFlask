from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import sqlite3

app = Flask(__name__)

app.database = "shoesorganizer.db"
app.secret_key = "xcFtjs3Ji896Ghm"


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap



@app.route('/')
def home():
	return render_template('index.html')


@app.route('/welcome')
@login_required
def welcome():
	g.db = connect_db()
	cur = g.db.execute('select * from shoescatalog')
	shoes = [dict(name=row[0], description=row[1], model=row[2] , image=row[3]) for row in cur.fetchall()]
	g.db.close()
	return render_template('welcome.html', shoes = shoes)


@app.route('/login', methods=['GET', 'POST'])
def login():
	error= None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':	
			error='Intente nuevamente'
		else:
			session['logged_in'] = True
			flash('Has iniciado sesion')
			return redirect(url_for('welcome'))
	return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('Has cerrado la sesion')
	return redirect(url_for('home'))


def connect_db():
	return sqlite3.connect(app.database)

