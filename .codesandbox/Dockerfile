FROM python:3.11.1

WORKDIR /app

# Copy only the requirements file initially
COPY requirements.txt .

# Create a virtual environment and install dependencies
RUN python -m venv venv && . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# CMD to run your application
CMD ["python", "main.py"]
