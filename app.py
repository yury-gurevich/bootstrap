# /usr/bin/python3

import os
from crypt import methods
from datetime import datetime
from enum import unique
from ssl import HAS_TLSv1_1

from flask import Flask, flash, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# secret_key = os.urandom(24)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SESSION_COOKIE_SECURE'] = True

# Initialise Database
db = SQLAlchemy(app)


# Create Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    date_added = db.Column(db.Date, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name


class NameForm(FlaskForm):
    name = StringField("What is your name: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


@app.route("/name", methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("form submitted successfully")

    return render_template("name.html", name=name, form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def special_error_handler(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
