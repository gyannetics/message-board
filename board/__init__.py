# Import necessary libraries
import os
from dotenv import load_dotenv
from flask import Flask

# Import blueprints and database module
from board import pages, posts, database

# Load environment variables from .env file
load_dotenv()

# Create Flask app
def create_app():
    app = Flask(__name__)

    # Load configuration from environment variables
    app.config.from_prefixed_env()

    # Initialize database
    database.init_app(app)

    # Register blueprints
    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)

    # Print current environment and database in use
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")

    return app
