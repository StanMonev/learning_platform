# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /learning_platform

# Copy the current directory contents into the container
COPY . /learning_platform

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000 6379

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]