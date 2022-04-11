# /usr/bin/python3

from crypt import methods
from ssl import HAS_TLSv1_1

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = "my secret key"


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

    return render_template("name.html", name=name, form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def special_error_handler(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
