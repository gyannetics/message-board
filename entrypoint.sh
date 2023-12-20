#!/bin/bash

# Load environment variables from .env file
if [ -f .env ]; then
    export $(cat .env | xargs)
fi

# Initialize the database
flask --app board init-db

# Run the Flask app
flask --app board run --port ${FLASK_RUN_PORT:-8000} --debug