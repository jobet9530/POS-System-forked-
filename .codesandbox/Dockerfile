FROM python:3.11.1

# Copy the files required for testing
COPY requirements.txt /app/requirements.txt
COPY /app/file.py /app/file.py
COPY /app/tests /app/tests

# Install the dependencies
RUN pip install -r requirements.txt

RUN python -m unittest discover /app/tests

# Run the tests
CMD ["python", "-m", "unittest", "discover", "-s", "app/tests", "app/tests", "-p", "test_*.py"]
