FROM python:3.11.1

# Copy the files required for testing
COPY requirements.txt /app/requirements.txt
COPY file.py /app/file.py
COPY tests /app/tests

# Install the dependencies
RUN pip install -r requirements.txt

# Run the tests
CMD ["python", "-m", "unittest", "discover", "-s", "app/tests", "-p", "test_*.py"]