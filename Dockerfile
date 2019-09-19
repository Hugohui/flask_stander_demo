FROM python:3.7
COPY . /app
WORKDIR /app

ADD requirements.txt /app/

RUN pip install -r requirements.txt

# web server config
EXPOSE 5203 50051