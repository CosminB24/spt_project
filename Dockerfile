FROM docker.io/library/python:3.9.18-alpine

WORKDIR /opt/app
ADD . /opt/app
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
