# Use a Python base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /usr/src/app

# Copy the necessary files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Copy and set permissions for the entrypoint script
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Use the entrypoint script to initialize and start the app
ENTRYPOINT ["./entrypoint.sh"]
