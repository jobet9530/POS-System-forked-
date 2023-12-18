FROM python:3.11.1

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV NAME python

CMD ["python","main.py"]