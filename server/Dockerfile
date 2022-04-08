FROM python:3.10

WORKDIR /app

ENV FLASK_ENV=development
ENV FLASK_APP=app.py
ENV PATH="/app/bin:${PATH}"

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py" ]
