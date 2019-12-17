from flask import render_template, url_for, flash, redirect, request
from blog import app, db, bcrypt
from blog.forms import registrationForm, loginForm
from blog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author' : 'Chinmay Badjatya',
        'title' : 'FirstPost' ,
        'content' : 'First Post stuff',
        'DatePosted' : '9th December',
    },
    {
        'author' : 'Elon Musk',
        'title' : 'SecondPost' ,
        'content' : 'SecondPost stuff',
        'DatePosted' : '9th December',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = registrationForm()
    if(form.validate_on_submit()):
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}, login now','success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = loginForm()
    if(form.validate_on_submit()):
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check your email and password.','danger')
    return render_template('login.html', title = 'Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    if not current_user:
        flash(f'You have to log in first','danger')
        return redirect(url_for('login'))
    else:
        return render_template("account.html", title="Account")
