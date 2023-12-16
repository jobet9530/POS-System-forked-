FROM python:3.11.1

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the working directory for the application
WORKDIR /app/.codesandbox

# CMD to run your application
CMD ["python", "main.py", "test_module.py"]
