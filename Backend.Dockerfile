# Use the alpine base image from Docker Hub
FROM alpine:latest

# Set the working directory
WORKDIR /app

# Install required packages for Python and Flask
RUN apk update && apk add python3 py3-pip

# Copy the application files to the container
COPY app.py requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=app.py

# Expose port 5000 to the outside
EXPOSE 5000

# Run the backend application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]