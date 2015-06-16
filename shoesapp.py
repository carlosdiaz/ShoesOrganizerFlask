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
