# Import the necessary Flask module
from flask import Blueprint, render_template

# Define a Flask blueprint for the pages
bp = Blueprint("pages", __name__)

# Define the home route that renders the home template
@bp.route("/")
def home():
    return render_template("pages/home.html")

# Define the about route that renders the about template
@bp.route("/about")
def about():
    return render_template("pages/about.html")
