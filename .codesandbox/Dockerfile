# Use the official Python image
FROM python:3.11.1

# Set the working directory
WORKDIR /app

# Copy only the requirements file initially
COPY ./requirements.txt .

# Create virtual environment
RUN python -m venv venv

# Activate virtual environment
SHELL ["/bin/bash", "-c"]
RUN source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the working directory for the application
WORKDIR .codesandbox

# CMD to run your application
CMD ["/app/venv/bin/python", "main.py", "test_module.py"]
