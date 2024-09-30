from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm, LoginForm


app = Flask(__name__, template_folder="template")
app.config["SECRET_KEY"] = "b4edff9631dcd00e3bf85f7e8ade241"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
db= SQLAlchemy(app)
app.app_context().push()


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),  nullable=False, default='default.jpg')
    password = db.Column(db.String(20), nullable=False)
    posts = db.relationship('Post', backref='author', lazy= True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime(20), nullable=False, default=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



posts = [
    {
        "author": "joe",
        "title": "blog post 1",
        "content": "first post",
        "date_posted": "march 30-2023",
    },
    {
        "author": "mark",
        "title": "blog post 2",
        "content": "second post",
        "date_posted": "april 4-2023",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("base.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}, success')
        return redirect(url_for('index'))
    return render_template("register.html", title="register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="login", form=form)


if __name__ == "__main__":
    app.run(debug=True)


