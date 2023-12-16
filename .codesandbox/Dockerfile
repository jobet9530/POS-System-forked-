FROM python:3.11.1

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the working directory for the application
WORKDIR /app/.codesandbox

# CMD to run your application
CMD ["python", "main.py", "test_module.py"]
