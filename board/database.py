import sqlite3
import click
from flask import current_app, g

# Function to initialize the app
def init_app(app):
    # Call close_db function when app context is torn down
    app.teardown_appcontext(close_db)
    # Add init_db_command to the CLI
    app.cli.add_command(init_db_command)

# Command line command to initialize the database
@click.command("init-db")
def init_db_command():
    # Get the database connection
    db = get_db()
    # Open schema.sql file and execute the SQL commands
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))
    # Print success message
    click.echo("You successfully initialized the database!")

# Function to get the database connection
def get_db():
    # Check if database connection exists in the app context
    if "db" not in g:
        # If not, create a new connection and store it in the app context
        g.db = sqlite3.connect(current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    # Return the database connection
    return g.db

# Function to close the database connection
def close_db(e=None):
    # Pop the database connection from the app context and close it
    db = g.pop("db", None)
    if db is not None:
        db.close()


'''
import sqlite3
import click
from flask import current_app, g

def init_app(app):
    app.cli.add_command(init_db_command)

@click.command("init-db")
def init_db_command():
    db = get_db()
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))
    click.echo("You successfully initialized the database!")

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop("db", None)
    if db is not None:
        db.close()
'''