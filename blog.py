from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == 'main':
    app.run(debug=True)
