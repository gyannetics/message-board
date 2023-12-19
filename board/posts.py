# Import necessary modules
from flask import Blueprint, redirect, render_template, request, url_for
from board.database import get_db

# Create a blueprint for the posts
bp = Blueprint("posts", __name__)

# Create a route for creating a new post
@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        # Get author and message from the form
        author = request.form.get("author", "Anonymous")
        message = request.form["message"]

        if message:
            # Insert the post into the database
            db = get_db()
            db.execute("INSERT INTO post (author, message) VALUES (?, ?)", (author, message))
            db.commit()
            # Redirect to the posts page
            return redirect(url_for("posts.posts"))

    # Render the create post page
    return render_template("posts/create.html")

# Create a route for viewing all posts
@bp.route("/posts")
def posts():
    # Get all posts from the database
    db = get_db()
    posts = db.execute("SELECT * FROM post").fetchall()
    # Render the posts page
    return render_template("posts/posts.html", posts=posts)
