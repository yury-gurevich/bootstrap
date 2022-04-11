# /usr/bin/python3

from ssl import HAS_TLSv1_1

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/name")
def user(name):
    return render_template("user.html", user=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def special_error_handler(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
