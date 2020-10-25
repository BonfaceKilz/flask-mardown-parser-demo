"""Bootstrap the app"""
import os

from flask import Flask
from flask import render_template

import mistune

app = Flask(__name__)
app.config.from_object("config")

basedir = os.path.abspath(os.path.dirname(__file__))

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    """Display this for any path that returns a 404"""
    return render_template('404.html', error=error), 404


@app.route("/", methods=["get"])
def index():
    """Display homepage which is normal html"""
    return render_template("index.html"), 200


@app.route("/test", methods=["get"])
def parse_markdown_from_file():
    """Parse markdown files from a file"""
    with open(os.path.join(basedir,
                           "markdown/introduction.md")) as md_file:
        markdown = md_file.read()
        return render_template("introduction.html",
                               rendered_markdown=mistune.html(markdown)), 200
