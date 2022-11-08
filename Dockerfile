# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-buster

RUN mkdir /app

WORKDIR /app/

ADD . /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "main:app" ]
