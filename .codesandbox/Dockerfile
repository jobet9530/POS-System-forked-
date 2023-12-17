# Use the official Python image
FROM python:3.11.1

# Set the working directory
WORKDIR /app

# Copy only the requirements file initially
COPY ./requirements.txt .

# Print the current directory and list the files for debugging
RUN pwd && ls -la

# Install dependencies, checking for missing modules
RUN pip install --no-cache-dir -r requirements.txt || (pip freeze | cut -d = -f 1 | xargs -n 1 pip install --no-cache-dir -U)

# Copy the rest of the application code
COPY . .

# Set the working directory for the application
WORKDIR .codesandbox

# CMD to run your application
CMD ["python", "main.py", "test_module.py"]
