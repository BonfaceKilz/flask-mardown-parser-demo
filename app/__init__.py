"""Bootstrap the app"""
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.config.from_object("config")


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    """Display this for any path that returns a 404"""
    return render_template('404.html', error=error), 404


@app.route("/", methods=["get"])
def index():
    """Display homepage which is normal html"""
    return render_template("index.html"), 200

