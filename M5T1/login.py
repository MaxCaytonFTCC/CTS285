# Minimal Flask App
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, g

DATABASE = 'database.db'

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def index():
    init_db()
    return redirect(url_for("login"))

@app.route("/welcome", methods=["GET"])
def welcome():
    return render_template("welcome_page.html")

@app.route("/registration", methods=["GET", 'POST'])
def registration():
    if request.method == 'POST':
        registered = create_user(request.form['username'], request.form['password'])
        if (registered == True):
            return redirect(url_for("login"))
        else:
             return render_template("registration_page.html",message="Email already in use")
    return render_template("registration_page.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if verify_login(request.form['username'], request.form['password']):
            return redirect(url_for('welcome'))
        else:
            return render_template('login_page.html',message="Invalid Username or Password")
    return render_template('login_page.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('login_page.html')

# Database Interfacing Methods
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (email TEXT PRIMARY KEY, password TEXT)''')
    c.execute('INSERT OR IGNORE INTO users VALUES (?, ?)',
              ('admin@example.com', 'admin123'))
    conn.commit()
    conn.close()

def verify_login(email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email=? AND password=?', 
              (email, password))
    result = c.fetchone()
    conn.close()
    return result is not None

def get_email_exists(email):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email=?', 
              (email,))
    result = c.fetchone()
    conn.close()
    return result is not None

def create_user(email ,password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT OR IGNORE INTO users VALUES (?, ?)',
            (email, password))
    
    # Check if user already exists
    if get_email_exists(email): return False

    c.execute(f'INSERT OR IGNORE INTO users VALUES (?, ?)',
              ('{email}', '{password}'))
    conn.commit()
    conn.close()
    return True


if __name__ == '__main__':
    init_db()
    app.run(debug=True)