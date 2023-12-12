FROM python:3.11.1

COPY requirements.txt /app/requirements.txt

COPY test/app/tests /app/tests

RUN pip install -r requirements.txt

RUN python -c "import <module_name> || pip install <module_name>"

CMD ["python","app.py"]