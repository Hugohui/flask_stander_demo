FROM python:3.7
COPY . /app
WORKDIR /app

ADD requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 5203

CMD python run.py