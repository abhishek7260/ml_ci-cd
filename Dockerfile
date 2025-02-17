# Use official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt file to the container
COPY requirements.txt /app/requirements.txt

# Install the dependencies in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the app's files to the container
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["flask", "run"]
