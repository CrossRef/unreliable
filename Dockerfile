# Use an official Python runtime as a parent image
FROM python:3.7


# Who to blame
MAINTAINER Geoffrey Bilder <gbilder@crossref.org>

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Upload source
COPY . $APP_HOME

# Make port 80 available to the world outside this container
EXPOSE 80

# run app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]