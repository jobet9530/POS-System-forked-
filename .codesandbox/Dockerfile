FROM python:3.11.1

COPY requirements.txt /app/requirements.txt

COPY . .

WORKDIR  /.codesandbox

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py", "test_module.py"]