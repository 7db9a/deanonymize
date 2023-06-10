# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt

ADD requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# This command will be run when the container starts
CMD ["python", "./deanonymize.py"]