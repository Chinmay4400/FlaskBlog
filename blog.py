from flask import Flask, render_template, url_for, flash, redirect
from forms import registrationForm, loginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '26ed3156048a4eb65dd07ce47fee898d'

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
    form = registrationForm()
    if(form.validate_on_submit()):
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = loginForm()
    if(form.validate_on_submit()):
        if(form.email.data == 'admin@blog.com' and form.password.data=='password'):
            flash(f'You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check your entries.','danger')
    return render_template('login.html', title = 'Login', form=form)

if __name__ == 'main':
    app.run(debug=True)
