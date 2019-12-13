from flask import Flask, render_template, url_for
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
    return render_template('register.html', title = 'Register', form=form)

@app.route("/login")
def login():
    form = loginForm()
    return render_template('login.html', title = 'Login', form=form)

if __name__ == 'main':
    app.run(debug=True)
