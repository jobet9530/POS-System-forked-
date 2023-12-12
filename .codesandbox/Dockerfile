FROM python:3.11.1

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

RUN python -c "import <module_name> || pip install <module_name>"

RUN python -m unittest discover -s /app/tests

RUN echo "Test Completed"

CMD ["python","app.py"]